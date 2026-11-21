#!/bin/sh
set -eu
cd "$(dirname "$0")"
{
  echo '$ uname -a'; uname -a
  echo; echo '$ cat /etc/os-release'; cat /etc/os-release
  echo; echo '$ stat -c ... README.md'; stat -c 'inode=%i size=%s blocks=%b block_unit=%B mode=%A' README.md
  echo; echo '$ df -i .'; df -i .
  echo; echo '$ ls -i README.md'; ls -i README.md
  echo; echo '$ df -T .'; df -T .
  echo; echo '$ tune2fs -l /dev/...'; 
  if command -v tune2fs >/dev/null 2>&1; then tune2fs -l "$(findmnt -no SOURCE /)" 2>&1 || true
  else echo 'NOT AVAILABLE: tune2fs is not installed in this execution environment; backing filesystem is overlayfs, not a directly inspectable ext filesystem.'; fi
  echo; echo '$ dumpe2fs -h /dev/...';
  if command -v dumpe2fs >/dev/null 2>&1; then dumpe2fs -h "$(findmnt -no SOURCE /)" 2>&1 || true
  else echo 'NOT AVAILABLE: dumpe2fs is not installed in this execution environment.'; fi
} | tee output/filesystem_evidence.txt
