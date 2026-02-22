#!/bin/bash
# PROTOCOL: SNiTE BoBy SYSTEM HEALTH REPORT
# FREQUENCY: Monthly (Cron-ready)

REPORT_FILE="/tmp/boby_health_$(date +%Y%m).log"
TRESPASS_FOUND=0

echo "--- [KING STATUS HEALTH AUDIT: $(date)] ---" > $REPORT_FILE

# 1. Audit Kod & Metadata Fail
echo "[SCANNING FILESYSTEM]" >> $REPORT_FILE
LEGACY_FILES=$(grep -rli "snitebobbie" . --exclude-dir={.git,node_modules,.venv} | wc -l)
if [ "$LEGACY_FILES" -gt 0 ]; then
    echo "ALERT: $LEGACY_FILES instances of legacy metadata found in files!" >> $REPORT_FILE
    TRESPASS_FOUND=1
fi

# 2. Audit Pangkalan Data (Contoh PostgreSQL)
echo "[SCANNING DATABASE]" >> $REPORT_FILE
DB_CHECK=$(psql -d snite_db -t -c "SELECT count(*) FROM artist_profiles WHERE display_name ILIKE '%bobbie%';" | xargs)
if [ "$DB_CHECK" -gt 0 ]; then
    echo "ALERT: $DB_CHECK legacy records found in artist_profiles!" >> $REPORT_FILE
    TRESPASS_FOUND=1
fi

# 3. Keputusan & Notifikasi
if [ $TRESPASS_FOUND -eq 1 ]; then
    echo "STATUS: COMPROMISED. Manual cleanup required." >> $REPORT_FILE
    # Opsyenal: Hantar e-mel atau notifikasi Telegram di sini
    # mail -s "KING STATUS ALERT: Legacy Detected" hafiz@example.com < $REPORT_FILE
else
    echo "STATUS: CLEAN. King Status is absolute." >> $REPORT_FILE
fi

cat $REPORT_FILE

