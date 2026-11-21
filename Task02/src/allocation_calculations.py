#!/usr/bin/env python3
BLOCK=4096
FILE=4*1024**3
N=FILE//BLOCK
PTR=4
P=BLOCK//PTR
inode_blocks=12+P+P**2+P**3
disk=4*1024**4
disk_blocks=disk//BLOCK
fat_bytes=disk_blocks*4
print(f"4 GiB file / 4 KiB blocks = {N:,} data blocks")
print(f"Reach last block: contiguous=1 data read; linked={N:,} block reads (follow chain); single index block cannot address this file")
print("Multi-level inode: with 12 direct + single/double/triple indirect, cached inode, triple-indirect lookup needs up to 4 reads (3 index blocks + data block)")
print(f"Pointers per 4 KiB index block: {P}")
print(f"Maximum inode blocks: 12 + {P} + {P**2:,} + {P**3:,} = {inode_blocks:,}")
print(f"Maximum inode capacity: {inode_blocks*BLOCK:,} bytes = {(inode_blocks*BLOCK)/1024**4:.6f} TiB")
print(f"4 TiB disk blocks: {disk_blocks:,}; 1-bit bitmap: {disk_blocks:,} bits = {disk_blocks//8:,} bytes = {disk_blocks//8/1024**2:.2f} MiB")
print(f"FAT at 4 bytes per block entry: {fat_bytes:,} bytes = {fat_bytes/1024**3:.2f} GiB RAM")
