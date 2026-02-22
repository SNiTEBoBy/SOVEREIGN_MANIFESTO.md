#!/bin/bash
# PROTOCOL: SNiTE BoBy IDENTITY HARDENING
# LEVEL: SYSTEM-WIDE FORCE ALIGNMENT

OLD_ID="snitebobbie"
NEW_ID="SNiTE BoBy"
NEW_ID_SLUG="SNiTEBoBy"

echo "--- [MEMULAKAN IDENTITY HARDENING: SNiTE BoBy] ---"

# 1. FORCE GIT CONFIG (GLOBAL)
echo "[1/4] Mengunci Konfigurasi Git Global..."
git config --global user.name "$NEW_ID"
git config --global core.excludesfile ~/.gitignore_global
echo "$OLD_ID" >> ~/.gitignore_global

# 2. FILE CONTENT OVERHAUL (SENSITIVE SEARCH)
echo "[2/4] Melaksanakan Penggantian Paksa pada Fail Teks..."
# Mencari semua fail teks dan mengganti tanpa mengira saiz huruf (case-insensitive)
find . -type f -not -path '*/.*' -exec grep -Iq . {} \; -print | xargs sed -i "s/$OLD_ID/$NEW_ID_SLUG/gI"

# 3. FILENAME REFACTORING
echo "[3/4] Menukar Nama Fail yang Mengandungi Identiti Lama..."
find . -name "*$OLD_ID*" -exec bash -c 'mv "$1" "${1//$OLD_ID/$NEW_ID_SLUG}"' -- {} \;

# 4. ENVIRONMENT VARIABLE CHECK
echo "[4/4] Mengimbas Fail .env dan Export..."
if [ -f .env ]; then
    sed -i "s/ARTIST_NAME=.*/ARTIST_NAME=\"$NEW_ID\"/g" .env
    sed -i "s/GITHUB_USER=.*/GITHUB_USER=\"$NEW_ID_SLUG\"/g" .env
fi

echo "--- [HARDENING SELESAI: SISTEM KINI SERIKAT DENGAN SNiTE BoBy] ---"
