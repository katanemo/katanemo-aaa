package main

import (
	authorizer_server "github.com/katanemo/katanemo-aaa/arc-go/arc/arc_server"
	"go.uber.org/zap"
)

func main() {
	cfg := zap.NewProductionConfig()
	// disable stack trace for now as it was causing too much spam in the logs
	cfg.EncoderConfig.StacktraceKey = ""
	logger := zap.Must(cfg.Build())
	undo := zap.ReplaceGlobals(logger)
	defer undo()

	zap.S().Infof("Initiating Server")
	if nil != authorizer_server.InitServer() {
		zap.S().Warnf("Failed to start server.")
	}
}
