#!/bin/sh
set -eu
cd "$(dirname "$0")"
gcc -std=c11 -Wall -Wextra src/sstf.c -o output/sstf
./output/sstf | tee output/scheduling_algorithms.txt
