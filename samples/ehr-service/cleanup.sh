#!/bin/sh

. ./common.sh

log destroying api stack
cdk destroy ApiLambdaEhrService

log destroying arc stack
pushd ../../arc-ecs/
cdk destroy ArcStack
popd
