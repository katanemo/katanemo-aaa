package authzparser

import (
	"fmt"

	"github.com/antlr/antlr4/runtime/Go/antlr"
	"github.com/golang-jwt/jwt/v5"
	parser "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/antlr"
)

func Evaluate(whereClause string, tags map[string][]string, claims jwt.MapClaims, reqObj map[string]interface{}) (bool, error) {
	is := antlr.NewInputStream(whereClause)

	lexer := parser.NewWhereConditionLexer(is)
	stream := antlr.NewCommonTokenStream(lexer, antlr.TokenDefaultChannel)

	p := parser.NewWhereConditionParser(stream)
	p.BuildParseTrees = true

	tree := p.Where_clause()

	var whereImpl AuthZWhereConditionListener
	whereImpl.ResourceTags = tags
	whereImpl.PrincipalTags = claims
	whereImpl.RequestObj = reqObj

	antlr.ParseTreeWalkerDefault.Walk(&whereImpl, tree)

	if whereImpl.IsError {
		return false, fmt.Errorf(whereImpl.Errors[0])
	}

	result, err := whereImpl.GetResult()
	if err != nil {
		return false, err
	}

	return result, nil
}
