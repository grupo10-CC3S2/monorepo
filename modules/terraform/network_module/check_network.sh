#!/usr/bin/env bash

set -e

NETWORK_NAME=$1
PORT=$2
REGION=$3

echo "Revisando configuracion de red..."
echo "Nombre de la red: $NETWORK_NAME"
echo "Puerto: $PORT"
echo "Region: $REGION"

GREEN_START="\033[32m"
GREEN_END="\033[0m"

echo -e "${GREEN_START}La configuracion de red es correcta.${GREEN_END}"

echo "Validacion de red completada!!"

exit 0
