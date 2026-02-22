#!/bin/bash
# PROTOCOL: SNiTE BoBy GLOBAL HOOK DEPLOYMENT
# TARGET: All Local Git Repositories

HOOK_CONTENT='#!/bin/bash
FORBIDDEN="snitebobbie"
STAGED_FILES=$(git diff --cached --name-only)
if [ -n "$STAGED_FILES" ]; then
    BAD_FILES=$(grep -iHn "$FORBIDDEN" $STAGED_FILES)
    if [ -n "$BAD_FILES" ]; then
        echo -e "\033[0;31m--- [CRITICAL: COMMIT REJECTED] ---\033[0m"
        echo "Identiti lama detected: $BAD_FILES"
        exit 1
    fi
fi
exit 0'

echo "--- [MEMULAKAN DEPLOYMENT GLOBAL: SNiTE BoBy GUARD] ---"

# Mencari semua direktori .git dalam direktori semasa (rekursif)
find . -name ".git" -type d | while read -r gitdir; do
    REPO_ROOT=$(dirname "$gitdir")
    HOOK_PATH="$gitdir/hooks/pre-commit"
    
    echo "Memasang Guard di: $REPO_ROOT"
    
    # Tulis kandungan hook
    echo "$HOOK_CONTENT" > "$HOOK_PATH"
    
    # Beri keizinan pelaksanaan
    chmod +x "$HOOK_PATH"
done

echo "--- [DEPLOYMENT SELESAI: SEMUA REPO DILINDUNGI] ---"

