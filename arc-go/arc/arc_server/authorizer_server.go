package authorizer_server

import (
	"fmt"
	"net/http"

	"github.com/brpaz/echozap"
	"github.com/caarlos0/env"
	"github.com/katanemo/katanemo-aaa/arc-go/arc/config"
	"github.com/katanemo/katanemo-aaa/arc-go/arc/internal/paths"
	"github.com/prometheus/client_golang/prometheus/promhttp"

	katlogger "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/auth/openapi"
	"github.com/labstack/echo-contrib/prometheus"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
	"go.uber.org/zap"
)

var ECHO *echo.Echo

func InitServer() error {
	cfg := &config.Settings{}
	if err := env.Parse(cfg); err != nil {
		panic(fmt.Sprintf("cannot parse env vars %v", err))
	}

	http.Handle("/metrics", promhttp.Handler())
	go func() {
		if err := http.ListenAndServe(fmt.Sprintf(":%v", cfg.ArcMetricPort), nil); err != nil {
			katlogger.Logger().Panic(fmt.Sprintf("cannot register prometheus handler: %v", err))
		}
	}()

	ECHO = echo.New()
	ECHO.Debug = true
	ECHO.HideBanner = true
	p := prometheus.NewPrometheus("auth", nil)
	p.Use(ECHO)

	ECHO.Pre(middleware.RemoveTrailingSlash())
	ECHO.Use(echozap.ZapLogger(zap.L()))
	devserver := paths.NewArcServer(cfg)
	openapi.RegisterHandlers(ECHO, devserver)

	bindPort := cfg.AuthArcPort

	ECHO.Logger.Fatal(ECHO.Start(fmt.Sprintf(":%s", bindPort)))
	return nil
}

func StopServer() error {
	ECHO = nil
	return ECHO.Close()
}
