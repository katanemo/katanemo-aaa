package paths

import (
	"fmt"
	"net/http"
	"os"
	"time"

	"github.com/MicahParks/keyfunc/v2"
	"github.com/golang-jwt/jwt/v5"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/db"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/keystore"

	"github.com/katanemo/katanemo-aaa/arc-go/arc/config"
	auth_core "github.com/katanemo/katanemo-aaa/arc-go/authorizer-core/paths"
	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"

	"github.com/labstack/echo/v4"
)

const KATANEMO_HTTP_HEADER_REQUEST_TIME = "X-Katanemo-Request-Time"

type ArcServer struct {
	authCore     auth_core.AuthorizerCore
	dataProvider db.AuthDataAccess
	GetPublicKey func() *keyfunc.JWKS
}

type ApplicationVersion struct {
	DeployedSha string `json:"deployed_sha"`
}

func (*ArcServer) GetHealthz(ctx echo.Context) error {
	deploySha := os.Getenv("DEPLOYED_SHA")
	return ctx.JSON(http.StatusOK, &ApplicationVersion{DeployedSha: deploySha})
}

func NewArcServer(settings *config.Settings) *ArcServer {

	arcDataFeeder := NewArcDataFeeder(settings)

	arcServer := ArcServer{
		dataProvider: arcDataFeeder,
		GetPublicKey: func() *keyfunc.JWKS {
			return arcDataFeeder.GetPublicKey()
		},
	}
	arcServer.initAuthCore()
	return &arcServer
}

func (dev *ArcServer) initAuthCore() {
	authCore := auth_core.NewAuthCore(dev.dataProvider, dev.ValidateToken)
	dev.authCore = *authCore
}
func (dev *ArcServer) AuthorizeRequest(ctx echo.Context) error {
	requestStartTime := time.Now()

	code, err := dev.authCore.AuthorizeRequest(ctx)

	if err != nil {
		katlogger.Logger().Errorf("authorization failed. Error: %v", err)
		return ctx.JSON(http.StatusInternalServerError, nil)
	}

	requestTimeMicroSec := fmt.Sprintf("%v", time.Since(requestStartTime).Microseconds())
	ctx.Response().Header().Add(KATANEMO_HTTP_HEADER_REQUEST_TIME, requestTimeMicroSec)
	return ctx.JSON(code, nil)
}

func (dev *ArcServer) ValidateToken(token string) (jwt.MapClaims, error) {

	jwks := dev.GetPublicKey()

	claims, err := jwt.Parse(token, jwks.Keyfunc)
	if err != nil {
		return nil, fmt.Errorf("failed to parse token: %w", err)
	}

	// Check if the token is valid.
	if !claims.Valid {
		return nil, fmt.Errorf("token is invalid")
	}

	parsedClaims, err := keystore.ParseTokenUnsafe(token)
	if err != nil {
		return nil, fmt.Errorf("token is invalid")
	}

	return parsedClaims, nil
}

func (dev *ArcServer) AddAccessLogs(ctx echo.Context) error {
	return fmt.Errorf("Shouldn't be implemented, only ARCOS should implement this.")
}
