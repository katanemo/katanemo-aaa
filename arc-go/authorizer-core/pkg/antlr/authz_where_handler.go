package authzparser

import (
	"fmt"
	"reflect"
	"strings"

	"github.com/antlr/antlr4/runtime/Go/antlr"
	"github.com/golang-jwt/jwt/v5"
	parser "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/pkg/core/antlr"
	katutils "github.com/katanemo/katanemo-aaa/arc-go/go-common-lib/utils"
)

type AuthZWhereConditionListener struct {
	*parser.BaseWhereConditionListener
	stack         katutils.Stack
	logicalStack  katutils.Stack
	ResourceTags  map[string][]string
	PrincipalTags jwt.MapClaims
	IsError       bool
	Errors        []string
	RequestObj    map[string]interface{}
}

func (this *AuthZWhereConditionListener) GetResult() (bool, error) {
	if this.logicalStack.Size() != 1 {
		return false, fmt.Errorf("Invalid evaluation")
	}
	return this.logicalStack.Pop().(bool), nil
}

func (s *AuthZWhereConditionListener) EnterWhere_clause(ctx *parser.Where_clauseContext) {

	s.stack = *katutils.NewEmptyStack()
	s.logicalStack = *katutils.NewEmptyStack()
}

func (this *AuthZWhereConditionListener) ExitComparison_operand(ctx *parser.Comparison_operandContext) {
	text := ctx.GetText()

	t := ctx.GetToken(parser.WhereConditionLexerRESOURCETAGS, 0)
	if t == nil {
		t = ctx.GetToken(parser.WhereConditionLexerPRINCIPALTAGS, 0)
	}
	if t == nil {
		t = ctx.GetToken(parser.WhereConditionLexerIDENTIFIER, 0)
	}
	if t == nil {
		t = ctx.GetToken(parser.WhereConditionLexerSTRING, 0)
	}
	if t == nil {
		t = ctx.GetToken(parser.WhereConditionLexerREQUEST, 0)
	}
	switch t.GetSymbol().GetTokenType() {
	case parser.WhereConditionLexerRESOURCETAGS:
		tag := strings.Split(text, ":")
		val := this.ResourceTags[tag[1]]
		if val == nil {
			str := []string{}
			this.stack.Push(str)
		} else {
			this.stack.Push(val)
		}
	case parser.WhereConditionLexerPRINCIPALTAGS:
		tag := strings.Split(text, ":")
		val := this.getClaim(tag[1])
		if val == nil {
			str := []string{}
			this.stack.Push(str)
		} else {
			this.stack.Push(val)
		}
	case parser.WhereConditionLexerREQUEST:
		tag := strings.Split(text, ":")
		val := this.getResourceFieldValue(tag[1])
		if val == "" {
			str := []string{}
			this.stack.Push(str)
		} else {
			str := []string{}
			str = append(str, val)
			this.stack.Push(str)
		}
	case parser.WhereConditionLexerIDENTIFIER:
		this.stack.Push(strings.ToLower(text))
	case parser.WhereConditionLexerSTRING:
		text = strings.ReplaceAll(text, "'", "")
		this.stack.Push(strings.ToLower(text))
	}
}
func (this *AuthZWhereConditionListener) ExitComparisonExpression(ctx *parser.ComparisonExpressionContext) {
	right := fmt.Sprintf("%v", this.stack.Pop())
	left := this.stack.Pop().([]string)
	this.logicalStack.Push(contains(left, right))
}

func (this *AuthZWhereConditionListener) ExitIn_list(ctx *parser.In_listContext) {

	var inlist []string = nil
	tokens := ctx.GetTokens(parser.WhereConditionLexerSTRING)
	for _, t := range tokens {
		txt := strings.ReplaceAll(t.GetText(), "'", "")
		inlist = append(inlist, strings.ToLower(txt))

	}
	this.stack.Push(inlist)
}

func (this *AuthZWhereConditionListener) ExitLogicalExpressionAnd(ctx *parser.LogicalExpressionAndContext) {
	right := this.logicalStack.Pop().(bool)
	left := this.logicalStack.Pop().(bool)
	this.logicalStack.Push(right && left)

}

func (this *AuthZWhereConditionListener) ExitLogicalExpressionOr(ctx *parser.LogicalExpressionOrContext) {
	right := this.logicalStack.Pop().(bool)
	left := this.logicalStack.Pop().(bool)
	this.logicalStack.Push(right || left)

}
func (this *AuthZWhereConditionListener) ExitIn_expression(ctx *parser.In_expressionContext) {
	invals := this.stack.Pop().([]string)
	tagValues := this.stack.Pop().([]string)

	for _, str := range tagValues {
		res := contains(invals, str)
		if res {
			this.logicalStack.Push(res)
			return
		}
	}
	this.logicalStack.Push(false)
}

func (this *AuthZWhereConditionListener) VisitErrorNode(node antlr.ErrorNode) {
	this.IsError = true
	this.Errors = append(this.Errors, node.GetText())
}

func contains(s []string, e string) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

func (this *AuthZWhereConditionListener) getClaim(claim string) []string {
	var retVal []string
	if _, ok := this.PrincipalTags[claim]; !ok {
		return retVal
	}

	if reflect.TypeOf(this.PrincipalTags[claim]).Kind() == reflect.Slice {
		claims := reflect.ValueOf(this.PrincipalTags[claim])
		for i := 0; i < claims.Len(); i++ {
			val := fmt.Sprintf("%v", claims.Index(i))
			retVal = append(retVal, val)
		}
	} else if reflect.TypeOf(this.PrincipalTags[claim]).Kind() == reflect.String {
		claims := reflect.ValueOf(this.PrincipalTags[claim])
		retVal = append(retVal, fmt.Sprintf("%v", claims))
	}
	return retVal
}

func (this *AuthZWhereConditionListener) getResourceFieldValue(field string) string {
	retVal := ""
	if this.RequestObj == nil {
		return retVal
	}
	fields := strings.Split(field, ".")
	fieldMap := this.RequestObj
	for _, f := range fields {
		val, ok := fieldMap[f]
		if !ok {
			return retVal
		}
		switch v := val.(type) {
		case map[string]interface{}:
			fieldMap = v
		case string:
			retVal = fmt.Sprintf("%v", v)
			return retVal
		default:
			return retVal
		}
	}
	return retVal
}
