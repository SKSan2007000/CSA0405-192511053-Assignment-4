#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 src/storage_calculations.py | tee output/storage_calculations.txt
