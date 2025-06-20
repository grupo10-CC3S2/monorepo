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

## [v0.2.0]
Para ambos archivos de todos los modulos se realiza un fix de nombre, se cambio de `computer_module` a `compute_module` y se realiza un cambio en la estructura de directorios para separar los tipos de archivos.

## [v0.4.0]

Se realizaron cambios en cada modulo en los archivos `output.tf` y `variables.tf` para mostrar informacion resumida de los recursos creados, estos se mostraran al ejecutar el comando `terraform apply` en el archivo `main.tf` principal. Tambien se agregan variable `version` para mostrar la version del modulo.

### Modulo network
Terraform:
- Se agrega output para mostrar informacion resumida de la red creada, con name, port y region.

### Modulo compute
Terraform:
- Se agrega output para mostrar informacion resumida del server creado, con name, network_name y count.

### Modulo storage
Terraform:
- Se agrega output para mostrar informacion resumida de la base de datos creada, con name, server_name y network_name.

## [v0.8.0]
Para todos los modulos se agregan scripts que simulan ejecucion de validacion, calculo de ID o backup, estos se ejecutan al simular la creacion de los recursos con `null_resource`, usando `local-exec` para ejecutar `python3` y `bash`.

### Modulo network
Terraform:
- Se agrega script `check_network.sh` que simula la validacion de la red creada, solo imprime mensajes de validacion.

### Modulo compute
Terraform:
- Se agrega script `calculate_id.py` que simula el calculo de un ID para el server creado, para esto usa `random.randint` de python e imprime informacion de cada server creado.

### Modulo storage
Terraform:
- Se agrega script `backup_database.sh` que simula la creacion de un backup de la base de datos creada, crea dos archivos txt, uno de log y otro de conteo de ejecucion.
- Para que el conteo de ejeciones funcione, se agrega `trigger` en `null_resource` con `timestamp()` de terraform, de esta manera siempre se disparara la simulacion de este recurso.

## [v1.0.0]
Despues de realizar test unitarios basicos, se realizaron test con validaciones de `port` e `instance_count`, ya que estos no pueden ser negativos o cero, se agregaron validaciones en los archivos `variables.tf` de cada modulo, ademas de validacion en los script generadores de `python` en las clases factory.

### Modulo network
Terraform y python:
- Se agrega validacion de `port` en `variables.tf` y `network.py` para que sea un numero entero mayor a 0 y menor a 65536.

### Modulo compute
Terraform y python:
- Se agrega validacion de `instance_count` en `variables.tf` y `server.py` para que sea un numero entero mayor a 0.

### Modulo storage
Terraform y python:
- Se modifica valor por defecto de `name` en `variables.tf`.
