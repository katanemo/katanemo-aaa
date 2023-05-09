package utils

import (
	"math/rand"
	"time"
)

// source https://stackoverflow.com/questions/22892120/how-to-generate-a-random-string-of-a-fixed-length-in-go
func init() {
	rand.Seed(time.Now().UnixNano())
}

var letterRunes = []rune("abcdefghjkmnopqrstuvwxyz")
var letterAndDigitsRunes = []rune("abcdefghjkmnpqrstuvwxyz23456789")

func RandStringRunes(n int) string {
	firstLetter := make([]rune, 1)
	firstLetter[0] = letterRunes[rand.Intn(len(letterRunes))]

	remainingLetters := make([]rune, n)
	for i := range remainingLetters {
		remainingLetters[i] = letterAndDigitsRunes[rand.Intn(len(letterAndDigitsRunes))]
	}

	return string(firstLetter) + string(remainingLetters)
}
