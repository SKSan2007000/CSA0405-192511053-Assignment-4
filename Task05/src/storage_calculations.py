#!/usr/bin/env python3
"""Transparent calculations for replicated storage and device-management notes."""
disk_bytes=4*1024**4
block_bytes=4*1024
blocks=disk_bytes//block_bytes
bitvector_bytes=blocks//8
print(f"Disk capacity: {disk_bytes:,} bytes (4 TiB)")
print(f"Block size: {block_bytes:,} bytes (4 KiB)")
print(f"Number of blocks: {blocks:,}")
print(f"Bit vector: {blocks:,} bits = {bitvector_bytes:,} bytes = {bitvector_bytes/1024**2:.2f} MiB")
print("\nReplication illustration for 100 TiB logical data:")
print("1 replica: 100 TiB raw; 3 replicas: 300 TiB raw (before metadata/reserve)")
print("If one replica fails, two remaining copies can serve reads while repair recreates redundancy.")
