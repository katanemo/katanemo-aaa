#!/bin/sh

wget https://www.antlr.org/download/antlr-4.7-complete.jar
java -jar ./antlr-4.7-complete.jar -Dlanguage=Go  -package parser *.g4
