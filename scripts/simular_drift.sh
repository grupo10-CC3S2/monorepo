#!/usr/bin/env bash

STATE_FILE="./environments/terraform/terraform.tfstate"

if [ ! -f "$STATE_FILE" ]; then
    echo "Error: El archivo de estado de Terraform no existe: $STATE_FILE"
    echo "Ejecutar terraform plan antes"
    exit 1
fi

echo "Simulando drift en el archivo de estado de Terraform: $STATE_FILE para el modulo de red..."

echo "Cambiando nombre de recurso en estado"
sed -i 's/"network-1"/"network-1000"/g' "$STATE_FILE"

echo "Cambiando puerto en estado"
sed -i 's/"port": 8080/"port": 5432/g' "$STATE_FILE"

echo "Drift simulado, habra diferencias de configuraciones, ejecutar terraform plan"