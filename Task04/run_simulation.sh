#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 src/simulation.py | tee output/simulation.txt
