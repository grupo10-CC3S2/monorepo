# Changelog - Monorepo

## [v0.1.0] - 2024-06-12

### Modulo network
Terraform:
- Version inicial que simula creacion de network usando `null_resource` y tomando dos variables de entrada `name` y `port`, se realiza output del nombre de la red creada y se imprime la creacion del recurso.

Python:
- Version inicial `network.py` que usa una clase constructora basada en el patron factory con parametros  name, port y da como salida un diccionario que se usara en `main.py` de directorio raiz para generar archivo `tf.json`, generando asi la configuracion de recurso compute, que sera usado finalmente para la creacion de este recurso.

### Modulo compute
Terraform:
- Version inicial que simula creacion de server usando `null_resource` y tomando variables de entrada `name`, `network_name` para mostrar la dependencia con la red creada inicialmente y `count` para la creacion de cierto numero de instancias, se realiza output del nombre del server creado y se imprime la creacion del recurso.

Python:
- Version inicial `server.py` que usa una clase constructora basada en el patron factory con parametros name, network_name e instance_count (con valor por defecto 1) y da como salida un diccionario que se usara en `main.py` de directorio raiz para generar archivo `tf.json`, generando asi la configuracion de recurso compute, que sera usado finalmente para la creacion de un servidor que depende de la creacion de red.

### Modulo storage
Terraform:
- Version inicial que simula creacion de database usando `null_resource` y tomando variables de entrada `name`, `network_name` y `server_name` para mostrar la dependencia con la red y server creadas y se realiza output del nombre de la db creado y su ruta y se imprime la creacion del recurso.

Python:
- Version inicial `database.py` que usa una clase constructora basada en el patron factory con parametros name, server y network (ambos son dependencias necesarias (compute, network) para la creacion del recurso de storage) y da como salida un diccionario que se usara en `main.py` de directorio raiz para generar archivo `tf.json` que sera usado finalmente para la creacion de una database que depende de la creacion de red y servidor
