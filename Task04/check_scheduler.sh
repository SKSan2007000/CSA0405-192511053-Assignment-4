#!/bin/sh
set -eu
{
  echo '$ ls /sys/block'; ls /sys/block
  for d in /sys/block/*; do
    if [ -r "$d/queue/scheduler" ]; then
      echo "$d: $(cat "$d/queue/scheduler")"
    fi
  done
} | tee output/scheduler_evidence.txt
