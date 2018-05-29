#!/bin/sh

for (( i = 1; i <= 15; i++))
do
    ./build/opt/zsim ./benchmarks/LRU/experiment$i.cfg
    python parser.py LRU.txt
done
for (( i = 1; i <= 15; i++))
do
    ./build/opt/zsim ./benchmarks/UCP/experiment$i.cfg
    python parser.py UCP.txt
done
for (( i = 1; i <= 15; i++))
do
    ./build/opt/zsim ./benchmarks/WPDIP/experiment$i.cfg
    python parser.py WPDIP.txt
done