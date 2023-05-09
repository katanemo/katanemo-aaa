package parser

import (
	"github.com/antlr/antlr4/runtime/Go/antlr"
)

type CoreWhereConditionListener struct {
	*BaseWhereConditionListener
	IsError bool
	Errors  []string
}

func (this *CoreWhereConditionListener) VisitErrorNode(node antlr.ErrorNode) {
	this.IsError = true
	this.Errors = append(this.Errors, node.GetText())
}
