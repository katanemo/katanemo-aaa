#!/bin/sh

. ./common.sh

log destroying api stack
cdk destroy ApiLambdaEhrService

log destroying arc stack
cdk destroy ArcStack
