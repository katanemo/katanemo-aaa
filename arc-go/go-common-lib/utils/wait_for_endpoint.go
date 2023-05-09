package utils

import (
	"net/http"
	"os"
	"time"
)

// WaitForEndpoint waits for an endpoint to be available

func WaitForEndpoint(endpoint string, retryCount int, waitBetween time.Duration) error {
	var err error
	for x := 0; x < retryCount; x++ {
		_, err = http.Get(endpoint)
		if err == nil {
			return nil
		}
		time.Sleep(waitBetween)
	}
	return err
}

func GetEnv(key, fallback string) string {
	if value, ok := os.LookupEnv(key); ok {
		return value
	}
	return fallback
}
