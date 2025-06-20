### Monorepo

Este monorepo contiene tres modulos de infraestructura para la simulacion de creacion de recursos en la nube. Cada modulo tiene su propio directorio y contiene archivos de Terraform `tf` y scripts de Python para la generacion de archivos `tf.json`.

Los entornos estan divididos en `environments/python` que usa imports locales de python para crear recursos con los 3 modulos de python, y `environments/terraform` que usa los modulos de terraform para crear los mismos recursos. Ambos se pueden ejecutar en cada directorio, ejemplo:

```sh
cd environments/python
python3 generate_infra.py
# se creo el archivo main.tf.json
terraform init
terraform plan
terraform apply -auto-approve
# se crearon los recursos
```

#### Setup

Para realizar la creacion de recursos, se requiere tener instalado Terraform y python. Sin embargo, se puede usar `devcontainer` para ejecutar los scripts y tests en este repositorio.

#### Ejecucion de terraform
Tambien, para ejecutar `main.tf` de `environments/terraform`, se tiene un archivo `Makefile` que permite ejecutar los comandos de terraform de manera sencilla. Los comandos disponibles son:

```sh
make # o make tf-init
make tf-plan # terraform plan
make tf-aa # terraform apply -auto-approve
make tf-ad # terraform destroy -auto-approve
```
Estos comandos se ejecutan desde la raiz del repositorio y se encargan de inicializar, planificar, aplicar y destruir los recursos de terraform.


### Ejecucion de scripts

Ambos scripts de bash que estan en el directorio `scripts` se pueden ejecutar directamente desde la raiz del repositorio.

- `rollback.sh`: Este script simula un rollback de los recursos creados usando git tags.

- `simular_drift.sh`: Este script simula un drift de los recursos creados, modificando el archivo `.tfstate`


#### Instalacion de dependencias
Estas librerias solo son necesarios para ejecutar tests y coverage, los scripts de python no usan librerias adicionales.

Si estas en windows:
```sh
# Creacion de entorno virtual
python -m venv venv
source venv\Scripts\activate # en git bash
pip install -r requirements.txt
```

Si estas en linux:
```sh
# Creacion de entorno virtual
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Ejecucion de tests
Para ejecutar tests de python, solo se usa:

```sh
pytest
```

ya que se usa `pytest.ini` para la configuracion de coverage y generacion de reporte en html.

Si se quiere ejecutar los tests de terraform, se puede usar el comando:

```sh
terraform test
```
desde la raiz del repositorio.


