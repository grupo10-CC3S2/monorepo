#!/usr/bin/env bash

set -e

MODULE_NAME=$1

MODULE_DIR="./modules/terraform/$MODULE_NAME"

if [ ! -d "$MODULE_DIR" ]; then
    echo "Error: Directorio del modulo no existe: $MODULE_DIR"
    exit 1
fi

VERSION=${2:-"v0.8.0"}

if [ -z "$MODULE_NAME" ]; then
    echo "Uso: $0 <nombre_modulo> [version]"
    echo "Modulos: compute_module, network_module, storage_module"
    echo "Ejemplo: $0 compute_module v0.4.0"
    exit 1
fi

TAG_NAME="$MODULE_NAME/$VERSION"

echo "Iniciando rollback del modulo de $MODULE_NAME..."
echo "Version objetivo: $VERSION"
echo "Tag: $TAG_NAME"

IS_TAG_VALID=$(git tag -l "$TAG_NAME")

if [ -z "$IS_TAG_VALID" ]; then
    echo "Error: tag $TAG_NAME no existe"
    exit 1
fi

CURRENT_DIR=$(pwd)

cd "$MODULE_DIR"

echo "Realizando rollback a version $VERSION..."
git checkout "$TAG_NAME" -- .

GREEN_START="\033[32m"
GREEN_END="\033[0m"

echo -e "${GREEN_START}Rollback del modulo $MODULE_NAME completado ok.${GREEN_END}"
echo "Ahora el modulo $MODULE_NAME esta en version $VERSION"

cd "$CURRENT_DIR"
exit 0
