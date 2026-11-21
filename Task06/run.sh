#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 src/design_simulation.py | tee output/design_simulation.txt
