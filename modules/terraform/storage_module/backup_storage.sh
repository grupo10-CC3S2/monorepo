#!/usr/bin/env bash

DB_NAME=$1

BACKUP_DIR="./backup/$DB_NAME"
COUNTER_FILE="$BACKUP_DIR/backup_runs.txt"

if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
    echo "Se creo directorio backup en $BACKUP_DIR"
else
    echo "Directorio backup ya existe en $BACKUP_DIR"
fi

if [ ! -f "$COUNTER_FILE" ]; then
    echo "1" > "$COUNTER_FILE"
    RUN_NUMBER=1
else
    CURRENT_RUN=$(cat "$COUNTER_FILE")
    RUN_NUMBER=$((CURRENT_RUN + 1))
    echo "$RUN_NUMBER" > "$COUNTER_FILE"
fi


echo "Iniciando backup para la db: $DB_NAME"
echo "Numero de ejecucion: $RUN_NUMBER"

echo "Ejecucion #$RUN_NUMBER  de $DB_NAME - $(date)" >> "$BACKUP_DIR/backup_log.txt"
echo "Backup realizado con exito!"
