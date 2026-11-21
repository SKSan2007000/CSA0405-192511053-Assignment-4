#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 src/test_simulation.py | tee output/boundary_test_results.txt
