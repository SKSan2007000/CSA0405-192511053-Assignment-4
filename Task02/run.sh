#!/bin/sh
set -eu
cd "$(dirname "$0")"
gcc -std=c11 -Wall -Wextra src/allocation.c -o output/allocation
./output/allocation | tee output/allocation.txt
