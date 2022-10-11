# App Recordatorio
## Clone repository
git clone  https://github.com/juandejunin/app_recordatorio.git

## Setup project win

### Install virtualenv
pip install virtualenv

### Create virtual environment
python -m virtualenv venv

### Activate virtualenv
.\venv\Scripts\activate

### Cuando vinculamos nuestro proyecto a base de datos y a cuentas de correo electronico estamos manejando informacion sensible, por lo tanto, tenemos que instalar una libreria que nos ayude a separar la informacion sensible del codigo que vamos a compartir y dejarla en una variable de entorno.

## Para este fin utilizaremos la libreria python-decouple.

### documentacion oficial de la libreria:
https://pypi.org/project/python-decouple/

### Instalar y configuar dependencias necesarias

### una vez dentro del entorno virtual:
### ejecutar
pip list
### para ver las dependencias que tenemos instaladas


### Install libraries inside virtualenv
### instalar las dependencias necesarias de forma automatica
pip install -r requeriment.txt
### esto instalaria todas las dependencias que contenga el archivo requeriment.txt


### Update requirements file
pip freeze > requirements.txt

### Corroborar la correcta instalacion de las dependencias necesarias.
pip list 

## Una vez instalado todo lo necesario pasamos a la configuracion:

### crear el archivo .env en el proyecto general

### copiar la llave secrect key en el archivo .env

SECRET_KEY = 'django-insecure-fk=y+dl0vgp5(bq4f_7uj@s4)_2i8fe7w@mpn^ctdh!r%6!uy2'

### copiar la configuracion del DEBUG ( para desarollo no para produccion):

DEBUG=True
## Configurar la base de datos externa antes del siguiente paso.
## Configuracion de la base de datos

NAME=app_recordatorio (el nombre que asignemos en la base de datos externas, se sugiere este para unificar)
USER=root
PASSWORD=xxxxxxxxxxxxxxxx
HOST=localhost
PORT=3306



### Run server
python manage.py runserver

## Setup project mac and linux
### Install virtualenv
pip3 install virtualenv

### Create virtual environment
python3 -m virtualenv venv

### Activate virtualenv
source venv/bin/activate

### Install Django inside virtualenv
pip3 install django

### Install Django rest inside virtualenv
pip3 install djangorestframework

### Run server
python3 manage.py runserver

# Config .env