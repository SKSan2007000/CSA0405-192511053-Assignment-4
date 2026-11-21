#!/bin/sh
set -eu
cd "$(dirname "$0")"
gcc -std=c11 -Wall -Wextra src/test_allocation.c -o output/test_allocation
./output/test_allocation | tee output/boundary_test_results.txt
