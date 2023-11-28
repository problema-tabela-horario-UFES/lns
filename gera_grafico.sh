#!/bin/bash
exec='python3 src/main.py' # ubuntu
input="tests/comp03.ctt"
output="results/graf"
timelimit="--timelimit=180"

echo "$exec <$input >$output"
$exec <$input >$output "--grafico" $timelimit