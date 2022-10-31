# RemindPay 
Bienvenidos a la plataforma de recordatorios de suscripciones de pago, encontrarás la guía de como implementar en tu entorno local y hacer pruebas. 
## Clonar repositorio
```
git clone  https://github.com/juandejunin/app_recordatorio.git
```
## Configuración del proyecto en windows

### Instalar el entorno  virtualenv
```
pip install virtualenv
```
### Crear el entorno virtual
```
python -m virtualenv venv
```
### Activar virtualenv
```
.\venv\Scripts\activate
```
## Instalar y configuar dependencias necesarias

### Una vez dentro del entorno virtual:

### Instalar las dependencias necesarias de forma automatica

#### Esto instalaria todas las dependencias que contenga el archivo requeriments.txt
```
pip install -r requirements.txt
```

### Ejecutar para ver las dependencias que tenemos instaladas
``` 
pip list 
```

### Actualizar las dependencias dentro del archivo requirements
- En caso de instalar más dependencias es necesario actualizar el archivo requirements.txt
- Para obtener los ultimos cambios en dicho archivo y volver a ejecutar e instalar y evitar errores por falta de esas librerias

```
pip freeze > requirements.txt
```
- No olvides ejecutar el comando;

```
pip install -r requirements.txt
```

## Explicación sobre la libreria python-decouple.

- Cuando vinculamos nuestro proyecto a base de datos y a cuentas de 
correo electronico estamos manejando informacion sensible, por lo tanto;
tenemos que instalar una libreria que nos ayude 
a separar la informacion sensible del codigo que vamos a compartir y 
dejarla en una variable de entorno.

## Documentación oficial de la libreria:
https://pypi.org/project/python-decouple/

## Una vez instalado todo lo necesario pasamos a la configuracion:

### Crear el archivo .env en el proyecto general
- SECRET_KEY: corresponde a la clave privada de python que genera al crear el proyecto
- DEBUG: debe permanecer en True solo cuando esta en desarrollo; por cuestiones de seguridad False en producción
- NAME: corresponde al nombre que asignemos en la base de datos externa
- USER: por defecto el usuario es root
- PASSWORD: contraseña en caso que posea
- HOST: localhost o una IP al cual conectarse
- PORT:  por defecto 3306 o en caso de que ese puerto se encuentre ocupado utilizar el 3307
```
SECRET_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
DEBUG=True
NAME=app_recordatorio
USER=root
PASSWORD=xxxxxxxxxxxxxxxx
HOST=localhost
PORT=3306
```

### Ejecutar el comando makemigrations 
- Este comando se encarga de crear nuevas migraciones en función de los cambios que haya realizado en sus modelos
```
python manage.py makemigrations
```

### Ejecutar las migraciones
- Este comando se encarga de aplicar y desaplicar migraciones (cambios para la base de datos).
```
python manage.py migrate
```

### Ejecutar el servidor
```
python manage.py runserver
```
## Configuración del proyecto en mac y linux
### Instalar virtualenv
```
pip3 install virtualenv
```
### Crear el entorno virtual 
```
python3 -m virtualenv venv
```
### Activar virtualenv
```
source venv/bin/activate
```
### Instalar las dependencias necesarias de forma manual
### Instalar Django dentro del virtualenv
```
pip3 install django
```
### Instalar Django rest dentro del virtualenv
```
pip3 install djangorestframework
```
### Instalar las dependencias necesarias de forma automatica

#### Esto instalaria todas las dependencias que contenga el archivo requeriments.txt
```
pip3 install -r requirements.txt
```

### Ejecutar para ver las dependencias que tenemos instaladas
``` 
pip3 list 
```

### Actualizar las dependencias dentro del archivo requirements
- En caso de instalar más dependencias es necesario actualizar el archivo requirements.txt
- Para obtener los ultimos cambios en dicho archivo y volver a ejecutar e instalar y evitar errores por falta de esas librerias

```
pip3 freeze > requirements.txt
```
- No olvides ejecutar el comando;

```
pip3 install -r requirements.txt
```


### Ejecutar el servidor
```
python3 manage.py runserver
```

## crear super usuario
 python manage.py createsuperuser



# API Rest Remindpay

### Funcionamiento de la API

## Endpoints registro y login

### Registro de usuario: 

```
http://127.0.0.1:8000/auth/users/
```

### Activar usuario: 

```
http://127.0.0.1:8000/auth/users/activation/ 
```
### Crear token de acceso:

```
http://127.0.0.1:8000/auth/jwt/create/
```
### Realizar refresh:
```
http://127.0.0.1:8000/auth/jwt/refresh/ 
```

### Verificar el refresh:
```
http://127.0.0.1:8000/auth/jwt/verify/
```

### Ver información del usuario:

 ```
http://127.0.0.1:8000/auth/users/me/
```

### Funcionamiento
La cabecera de POST se configura de la siguiente manera:
- KEY: Content-Type
- VALUE: application/json

### Registro de usuario: 
```
http://127.0.0.1:8000/auth/users/
```

### Se esperan los siguientes datos:

```
{
    "email":"tu_email@gmail.com",
    "first_name":"tu_nombre",
    "last_name":"tu_apellido",
    "password":"tu_contraseña",
    "re_password":"tu_contraseña"
}
```

### Una vez hecho el registro llegara a el correo electronico un link similar al siguiente:

```
http://127.0.0.1:8000/activate/MQ/bdyjyt-95cd1361339c1ef5638bfb69c502caea
```

### De este link se estraeran dos codigos. 
- El primero es el contiguo a http://127.0.0.1:8000/activate/ en este caso
```
MQ
```
 
-  El segundo codigo es el que continua despues de este:

```
bdyjyt-95cd1361339c1ef5638bfb69c502caea
```

-  Estos codigos se extraen para ingresarlos de la siguiente forma en el endpoint 

### Activar usuario: 

```
http://127.0.0.1:8000/auth/users/activation/ 
```
### Espera los siguientes datos:
```
{
    "uid":"MQ",
    "token":"bdyjyt-95cd1361339c1ef5638bfb69c502caea"
}
```
### Si se realizo todo de forma correcta se recibira un nuevo correo informando que la cuenta fue activada

Your account has been created and is ready to use!
Thanks for using our site!

### El siguiente endpoint nos permite crear el token de acceso

### Crear token de acceso:

```
http://127.0.0.1:8000/auth/jwt/create/
```
### Espera los siguientes datos:
```
{
    "email":"juancito@gmail.com",
    "password":"contra123"
}
```

 ### Retorna dos codigos, el refresh y el access
- Resfresh: nos permite continuar logueados dentro del navegador
- Access: es el token que necesitaremos para ingresar a nuestra cuenta

```
 {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2OTQ2Nzg2NSwianRpIjoiYThlNjIwMWZjMDJmNGNlMDk3YmEzYWY3ZDhlMzQ4OGIiLCJ1c2VyX2lkIjoxfQ.lkpJ7J4EchVMcjHB8lUvubI9ElY0N2dnxMs5eNgwOgg",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3NDgwNjY1LCJqdGkiOiI5MmI5OTNmYmNmOTg0MGI3YjAzOTdiMTEyZjRjZWY5MyIsInVzZXJfaWQiOjF9.whWaaM7iK1tDJkWvm-WS3WGi6FGkWZFjGuuudEsLQAg"
 }
```


## Login

### En este caso es una peticion GET y en la cabecera usaremos la siguiente configuracion

- KEY: Authorization
- Value: tipeamos JWT dejamos un espacio y el token obtenido  
```
VALUE : JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3NDgwNjY1LCJqdGkiOiI5MmI5OTNmYmNmOTg0MGI3YjAzOTdiMTEyZjRjZWY5MyIsInVzZXJfaWQiOjF9.whWaaM7iK1tDJkWvm-WS3WGi6FGkWZFjGuuudEsLQAg
```







