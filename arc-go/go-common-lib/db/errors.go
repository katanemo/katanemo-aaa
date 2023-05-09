package db

import "errors"

var ErrDeveloperNotFound = errors.New("developer not found")
var ErrClientKeyNotFound = errors.New("client key not found")
var ErrServiceNotFound = errors.New("service not found")
var ErrMetadataNotFound = errors.New("metadata not found")
var ErrDeveloperNotWithWithService = errors.New("developer not with with service")
