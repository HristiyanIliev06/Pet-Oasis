#!/usr/bin/env bash
set -euo pipefail

BACKUP_DIR="${BACKUP_DIR:-$HOME/petoasis-backups}"
DB_NAME="${DB_NAME:-pet_oasis_db}"
DB_USER="${DB_USER:-petoasis}"
DB_HOST="${DB_HOST:-127.0.0.1}"
: "${DB_PASSWORD:?DB_PASSWORD is not set}"

mkdir -p "$BACKUP_DIR"
FILE="$BACKUP_DIR/${DB_NAME}-$(date +%Y%m%d-%H%M%S).sql.gz"

PGPASSWORD="$DB_PASSWORD" pg_dump -h "$DB_HOST" -U "$DB_USER" "$DB_NAME" | gzip > "$FILE"
echo "Backup written to $FILE ($(du -h "$FILE" | cut -f1))"

# keep only the 5 newest backups
ls -1t "$BACKUP_DIR"/*.sql.gz | tail -n +6 | xargs -r rm --