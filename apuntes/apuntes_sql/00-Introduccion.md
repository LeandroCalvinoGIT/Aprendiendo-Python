# BASES DE DATOS

## QÚE SON?

"Conjunto de información almacenado y consultado sistemáticamente"

Una base de datos es un lugar organizado para guardar información de forma:
- persistente (no se pierde al cerrar el programa)
- estructurada
- fácil de consultar y modifica

Los datos están interrelacionados, son consultados concurrentemente.

## TABLAS

Una tabla es como una hoja de excel, representa una entidad (una clase o un objeto).
Cada fila sigue una estructura (es una instancia), y cada columna representa un tipo de dato(un atributo)

## TIPOS DE DATOS

Los tipos de datos sirven para:
- ahorrar espacio
- evitar errores
- permitir búsquedas eficientes

SQL         /	Similar en Python
INTEGER	        int
TEXT	        str
REAL	        float
BOOLEAN	        bool
DATE	        datetime/date

📌 No todo es texto, aunque podría serlo
👉 usar tipos correctos = mejor performance + menos errores

## Clave primaria

Es una columna o conjunto de columnas que **identifican** cada fila (como el id)

Reglas:
- No se repite
- No es nula
- Identifica exactamente a un solo registro

## SISTEMA GESTOR DE BASE DE DATOS (SGBD)

Mientras que la base de datos es la info, el sistema es un software que permite organizar y consultar (búsquedas) dicha info:
- Definen estructuras de datos
- Permiten manipular dichos datos
- Mantienen integridad de la info
- Garantizan Privacidad y seguridad

Ejemplos de SGBD
- SQLite
- MySQL
- PostgreSQL
- SQL Server

Python no habla con la base directamente, habla con el SGBD.

##  BASES DE DATOS RELACIONES

Son bases en las que los datos están en **tablas** que pueden relacionarse entre sí-

- Manejan modelos de entidad relación:
- En estas, cada entidad o clase (ej: alumnos, cursos, profesores) se guardan en una **tabla**
- En cada tabla, cada entidad se guarda en un **registro**
- Cada registro tiene distintos campos (ej: Alumnos: nombre, apellido, edad, pais, mail)
- En resumen: Los datos se guardan en **TABLAS** en las que las *filas* son **REGISTROS**, y las *columnas* **CAMPOS**, y para realizar búsquedas se establecen **relaciones** entre dichas tablas

📌 Ideal para:
- sistemas backend
- datos estructurados
- integridad y consistencia

# Bases de datos NO RELACIIONALES

Sin estructuras definidas, puede haber redundancia de datos, pero este tipo de BDD prioriza el acceso rápido sobre la normalización. La diferencia solo se nota en altísima demanda:
- algunas apps necesitan flexibilidad
- grandes volúmenes
- datos semi-estructurados
EJ MongoDB, NoSQL (Not only SQL)

# SQL: Structured Query Language

Lenguaje de BDD relacionales conformado por 3 sublenguajes:
- DATA DEFINITION LANGUAGE (DDL): Define las estructuras
- DATA MANIPULATION LANGUAGE (DML): Escribe, lee, actualiza, y borra datos de las tablas
- DATA CONTROL LANGUAGE (DCL): Controla los permisos de acceso a las bases de datos

Es un lenguaje **declarativo**, por lo que solo hay que declarar el "qué" y no el "cómo""

## ID

     id: primary key
name_id: foreign key



## SENTENCIAS

### DML
- SELECT: 
- INSERT
- DELETE
- UPDATE

### DDL
- CREATE
- DROP
- ALTER

# SQL + PYTHON = SQlite

En python existe el modulo **sqlite3**.
SQLite es un motor de base de datos relacional embebido, por lo que no requiere un servidor.

Para iniciar y crear la conexión con la bdd:

```python
import sqlite3
conexion = sqlite3.connect("nombre_base")
cursor = conexion.cursor() # Permite ejecutar los comandos SQL
conexion.close()
```

