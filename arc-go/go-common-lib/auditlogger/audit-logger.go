package auditlogger

import (
	"sync"

	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/logger"
	"github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/auth/openapi"
	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
	"gopkg.in/natefinch/lumberjack.v2"
)

var auditLogger *zap.Logger

func InitAuditLogger() {
	encoderConfig := zapcore.EncoderConfig{
		MessageKey:   "message",
		LevelKey:     "level",
		TimeKey:      "timestamp",
		EncodeTime:   zapcore.ISO8601TimeEncoder,
		CallerKey:    "caller",
		EncodeCaller: zapcore.ShortCallerEncoder,
		// Add the custom fields to the encoder configuration
		EncodeDuration: zapcore.StringDurationEncoder,
		EncodeName:     zapcore.FullNameEncoder,
	}
	encoder := zapcore.NewJSONEncoder(encoderConfig)

	core := zapcore.NewCore(encoder, zapcore.AddSync(&lumberjack.Logger{
		// Filename:   "/var/log/aaa/audit/authz.log",
		Filename:   "/tmp/authz.log",
		MaxSize:    10, // MB
		MaxBackups: 3,
		MaxAge:     28, // days
	}), zap.InfoLevel)

	auditLogger = zap.New(core, zap.AddCaller())
}

func CloseAuditLogger() {
	if auditLogger != nil {
		if auditLogger.Sync() != nil {
			logger.Logger().Error("Failed to sync events logger")
		}
	}
}

var once sync.Once

func AuditLogger() *zap.Logger {
	once.Do(func() {
		InitAuditLogger()
	})
	return auditLogger
}

type AuditLogEntry struct {
	Version string
	openapi.AuditLogEntry
	// requestParams            map[string]string
	// policyEvaluationSegments map[string]string
	// policyId                 string
	// resourceTags             map[string]string
	// principalTags            map[string]string
}

func AuditLog(logEntry *AuditLogEntry) {

	// version int, accountId string, serviceId string, principal string, path string, operation string, requestParams map[string]string, authHttpCode int, authzHttpCode int, policyEvaluationSegments map[string]string, policyId string, resourceTags map[string]string, principalTags map[string]string

	// msg := map[string]interface{}{
	// 	"version": version,
	// 	"principal": principal,
	// 	"path": path,
	// 	"operation": operation,
	// 	"request-parameters": requestParams,
	// 	"authentication-http-code": authHttpCode,
	// 	"authorization-http-code": authzHttpCode,
	// 	"policy-evaluation-segments": policyEvaluationSegments,
	// 	"policy-id": policyId,
	// 	"resource-tags": resourceTags,
	// 	"principal-tags": principalTags,
	// }

	// AuditLogger().Info(msg)
	AuditLogger().Info("Authorization log",
		zap.String("version", logEntry.Version),
		zap.String("accountId", logEntry.AccountId),
		zap.String("serviceId", logEntry.ServiceId),
		zap.String("principal", logEntry.Principal),
		zap.String("path", logEntry.Path),
		zap.String("operation", logEntry.Operation),
		zap.Int("authenticationCode", logEntry.AuthenticationCode),
		zap.Int("authorizationCode", logEntry.AuthorizationCode),
		// zap.Any("request-parameters", requestParams),
		// zap.Any("policy-evaluation-segments", policyEvaluationSegments),
		// zap.String("policy-id", policyId),
		// zap.Any("resource-tags", resourceTags),
		// zap.Any("principal-tags", principalTags),
	)
}
