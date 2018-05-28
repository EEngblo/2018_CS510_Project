#!/bin/sh

for (( i = 1; i <= 15; i++))
do
    ./build/opt/zsim ./benchmarks/experiment$i.cfg
    python parser.py result$i.txt
done