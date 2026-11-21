#include <assert.h>
#include <stdio.h>
#include <string.h>
#define main allocation_demo_main
#include "allocation.c"
#undef main
int main(void) {
    int idx[BLOCKS];
    memset(disk,'.',BLOCKS);
    assert(alloc_contiguous('X',0)==-1);
    assert(alloc_contiguous('X',BLOCKS+1)==-1);
    assert(alloc_contiguous('X',4)==0);
    memset(disk,'.',BLOCKS);
    for (int i=0;i<20;i++) disk[i]='Z';
    assert(alloc_indexed('Y',12,idx)==-1);
    puts("PASS: zero-size, oversized, first-fit and insufficient-index-space tests");
    return 0;
}
