# SonidoCloud

Proyecto No. 1 para CC3057 Bases de Datos - UVG 2020

Desarrollado usando python 3.6.9 con PostgreSQL, usando ```psycopg2``` para la conexión con la base de datos, y ```PyQt``` para la interfaz gráfica.

## Uso

Es necesario instalar paquetes previamente, este es un proceso sencillo usando ```pip```:

```bash
$ pip install pyqt5
```
```bash
$ pip install psycopg2
```
Si no funciona psycopg2 probar:
```bash
$ pip install psycopg2-binary
```
```bash
$ pip install fpdf
```

Luego, montar en la base de datos de POSTGRES, el archivo ```Proyecto1.sql```.

Finalmente, para ejecutar la aplicación, correr el acrchivo ```Loginaccount.py```:


## Importante

Para que el sistema se concecte correctamente con la base de datos, es importante que el usuario agregue sus credenciales en el archivo ```base_de_datos.ini``` ubicado en el directorio principal. En este archivo se deben ingresar las credenciales indicadas (host, database, user, password, port) **sin el uso de comillas**. Ejemplo:
``` bash
host = 127.0.0.1
database= testdb
user= postgres
password= 12345678
port= 5432
```
se conectará a la base de datos ```testdb``` en el host ```127.0.01```, puerto ```5432``` como el usuario ```postgres``` y la contraseña ```12345678```.

## Integrantes

Marco Fuentes

Andy Castillo

Michele Benvenuto

Cristina Bautista
