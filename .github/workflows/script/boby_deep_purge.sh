#!/bin/bash
# PROTOCOL: SNiTE BoBy DEEP PURGE
# TARGET: Hidden cache, logs, and temp files

echo "--- [MEMULAKAN PURGE TERSEMBUYI: SNiTE BoBy] ---"

# Membersihkan cache VS Code, Git, dan fail sementara sistem
find . -name ".DS_Store" -delete
find . -name "*.log" -exec grep -l "snitebobbie" {} + | xargs rm -f
git gc --prune=now --aggressive

echo "--- [PURGE SELESAI: KING STATUS IS ABSOLUTE] ---"

