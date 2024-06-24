# prueba_1_FastAPI
Servicio sencillo en FastAPI que se conecta a una base de datos psql.

## Configuración del Entorno Virtual y Requisitos

#### Requisitos previos

Si no se tiene el equipo configurado adecuadamente la instalación de paquetes fallará, se recomienta tener instalado:

```bash
sudo apt-get install python3-dev
sudo apt-get install libpq-dev
```

#### Creación de un Entorno Virtual (Opcional)

Si deseas utilizar un entorno virtual para gestionar las dependencias de este proyecto de manera aislada, sigue estos pasos:

##### Linux

```bash
# Instala virtualenv si no está instalado
pip install virtualenv 
# Crea un nuevo entorno
virtual virtualenv venv # o python3 -m venv venv
# Activa el entorno virtual
source venv/bin/activate
```
##### Windows

```bash
# Instala virtualenv si no está instalado 
pip install virtualenv 
# Crea un nuevo entorno virtual 
virtualenv venv 
# Activa el entorno virtual 
venv\Scripts\activate
```
#### Instalación de Dependencias

Instala las dependencias necesarias utilizando `pip` y el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```
Este comando instalará todas las bibliotecas requeridas para ejecutar la aplicación, incluyendo FastAPI, psycopg2, pandas, entre otras especificadas en el archivo `requirements.txt`.

Una vez completados estos pasos, podrás ejecutar el proyecto de manera aislada dentro del entorno virtual configurado, asegurando la compatibilidad y gestión eficiente de las dependencias.

## Descripción del Código

Este repositorio contiene un conjunto de scripts y archivos para interactuar con una base de datos PostgreSQL utilizando Python, utilizando tanto el módulo psycopg2 como pandas para ejecutar consultas SQL y manejar errores de conexión y consulta de manera efectiva.
## Archivos y Scripts

- **create_database.sh**: Script para crear una base de datos PostgreSQL y configurar un usuario con privilegios adecuados. Se puede ejecutar para preparar el entorno antes de usar la aplicación principal.

- **fill_database.sh**: Script para llenar la base de datos con datos ficticios, específicamente con información simulada del Producto Interno Bruto per cápita de países desde 1980.

- **main.py**: Código principal de la aplicación FastAPI. Define rutas y operaciones para interactuar con la base de datos, utilizando Swagger para documentación y Redoc para visualización.

- **create_and_fill_table.py**: Contiene funciones para crear y llenar tablas en la base de datos utilizando consultas SQL predefinidas.

- **constants.py**: Define constantes y configuraciones, incluyendo variables de entorno para la conexión a la base de datos.

- **environment.py**: Gestiona las variables de entorno para la configuración segura de la base de datos.

## Manejo de Errores y Conexión

- **Errores de Conexión y Consulta**: Todas las conexiones a la base de datos y las consultas SQL están protegidas dentro de bloques `try-except`. Si ocurre un error de conexión o una consulta falla, se captura la excepción y se maneja adecuadamente para evitar interrupciones en el servicio.

- **Uso de finally**: Se utiliza finally para asegurar que las conexiones a la base de datos siempre se cierren correctamente después de realizar operaciones, garantizando una gestión adecuada de recursos y evitando posibles problemas de memoria o bloqueos.

## Uso de psycopg2 y pandas

- **psycopg2**: Utilizado para establecer conexiones directas a la base de datos PostgreSQL y ejecutar consultas SQL de manera eficiente y directa.

- **pandas**: Utilizado para cargar datos desde la base de datos PostgreSQL en un DataFrame, lo que facilita el análisis y la manipulación de datos utilizando funcionalidades avanzadas de pandas.

## Ejecución y Documentación

### Para ejecutar y documentar la aplicación:

Los archivos deben tener permiso de ejecución, en linux:

```bash
sudo chmod +x <name>.sh
```

- **Preparación de la Base de Datos**:
    Ejecuta create_database.sh si la base de datos no está configurada previamente. Este script establecerá la base de datos y configurará el entorno. 

- **Llenado de la Base de Datos**:
    Utiliza fill_database.sh para llenar la base de datos con datos simulados del Producto Interno Bruto per cápita de países.

- **Ejecución de la Aplicación**:
    Inicia la aplicación FastAPI ejecutando main.py. Accede a /docs o /redoc para ver la documentación automática generada por Swagger o Redoc, respectivamente, y administra la API.

**En local**:

```bash
python3 main.py
```
