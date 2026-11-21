#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 src/allocation_calculations.py | tee output/allocation_calculations.txt
