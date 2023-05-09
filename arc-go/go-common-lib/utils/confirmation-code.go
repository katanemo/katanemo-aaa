package utils

import (
	"crypto/sha1"
	"encoding/base64"
	"io"
)

func GenerateDevConfirmationCode(email, accountId string) string {
	h := sha1.New()
	if _, err := io.WriteString(h, email); err != nil {
		panic(err)
	}
	if _, err := io.WriteString(h, accountId); err != nil {
		panic(err)
	}
	temp := h.Sum(nil)
	sEnc := base64.URLEncoding.EncodeToString(temp)
	return sEnc
}
