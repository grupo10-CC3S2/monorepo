#!/usr/bin/env python3

import sys
import random


def simulate_calculation(instance_number):
    dummy_result = random.randint(1, 100) * instance_number
    return dummy_result


def main():
    if len(sys.argv) != 5:
        print("Uso: python3 compute_tool.py <nombre_instancia> <nombre_network> <numero_instancia> <region>")
        sys.exit(1)

    instance_name = sys.argv[1]
    network_name = sys.argv[2]
    instance_count = int(sys.argv[3])
    region = sys.argv[4]

    print("Configurando server...")
    print(f"Nombre del server: {instance_name}")
    print(f"Numero de servers: {instance_count}")
    print(f"Nombre de la red: {network_name}")
    print(f"Region: {region}")

    result = simulate_calculation(instance_count)

    print(f"ID generada del servidor: {result}")
    print("Configuracion del server completada con exito!")


if __name__ == "__main__":
    main()
