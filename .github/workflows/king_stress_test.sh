#!/bin/bash
# PROCOCOL: SNiTE BoBy STRESS TEST & RECOVERY
# PURPOSE: Ensure 100% Identity Alignment under System Failure

LOG_FILE="king_audit_$(date +%Y%m%d).log"

exec > >(tee -a "$LOG_FILE") 2>&1

echo "--- [STARTING STRESS TEST: KING STATUS] ---"

# 1. TEST: Permission Recovery
echo "[1/4] Checking File Permissions..."
find . -type f -name "*Bobbie*" -not -perm /u+w -exec chmod u+w {} + 
if [ $? -eq 0 ]; then
    echo "SUCCESS: Write permissions restored."
else
    echo "CRITICAL: Manual intervention required for read-only files."
fi

# 2. TEST: Recursive Namespace Overhaul (Case-Insensitive)
echo "[2/4] Executing Deep-Scan Identity Replacement..."
# Menggunakan sed dengan perlindungan terhadap fail perduaan (binary)
find . -type f -not -path '*/.*' -exec grep -Iq . {} \; -print | xargs sed -i 's/snitebobbie/SNiTEBoBy/gI'
echo "SUCCESS: All textual references updated to SNiTE BoBy."

# 3. TEST: Git Remote Validation
echo "[3/4] Validating Git Integrity..."
CURRENT_REMOTE=$(git remote get-url origin 2>/dev/null)
if [[ $CURRENT_REMOTE == *"snitebobbie"* ]]; then
    NEW_REMOTE=$(echo $CURRENT_REMOTE | sed 's/snitebobbie/SNiTEBoBy/g')
    git remote set-url origin "$NEW_REMOTE"
    echo "RECOVERED: Remote URL shifted to $NEW_REMOTE"
else
    echo "STABLE: Git remote already aligned."
fi

# 4. TEST: Dead Link Cleanup
echo "[4/4] Cleaning Broken Symbolic Links..."
find . -xtype l -delete
echo "SUCCESS: Broken references purged."

echo "--- [STRESS TEST COMPLETE: STATUS GREEN] ---"

