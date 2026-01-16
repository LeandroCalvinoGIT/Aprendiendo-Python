# TIPOS DE DATOS

- INTEGER: numero entero con signo, el rango depende del tamaño definido, para campos que representan cantidad
    - TINYINT:   (-128, 127)
    - SMALLINT:  (-32768, 32757)
    - MEDIUMINT: ()
    - INT:       ()
    - BIGINT:    ()

- TEXT: strings, cadenas de caracteres

- NULL: representan la falta de información o información desconocida

- REAL: numero reales con valores decimales:
    - REAL
    - DOUBLE
    - DOUBLE PRESICION
    - FLOAT

- BLOB: objeto binario de gran tamaño que puede almacenar cualquier tipo de dato
  - imagenes
  - musica
  - documentos
  - pdf
  - otros

# CURSOR

Es un objeto de acceso a datos que permite que python ejecute sentencias SQL. Está vinculado a la conexión durante todo el tiempo y todos los comandos se ejecutan en la base de datos

Se crea: ```conexion.cursor()```

```python
import sqlite3
conexion = sqlite3.connect("nombre_base")
cursor = conexion.cursor() # Permite ejecutar los comandos SQL
cursor.execute("""
                COMANDOS SQL
                
                """)
conexion.close()
```
# COMANDOS
C: create
R: read
U: update
D: delete

Query: Consulta

## CREATE TABLE

Permite crear una tabla en la BDD ya existente:

CREATE TABLE IF NOT EXISTS nombre_tabla(columna1 TIPO, columna2 TIPO)

EJ: 

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER,
    ciudad TEXT
)
""")
```

## INSERT

Permite ingresar datos en la tabla:

INSERT INTO nombre_tabla(columna1,columna2,columna3)
VALUES
    (datocolumna_1,dato_columna2,dato_columna3)

EJ:
```python
cursor.execute("""
INSERT INTO usuarios (nombre, edad, ciudad)
VALUES 
    ('Ana', 30, 'Córdoba'),
    ('Juan', 25, 'Buenos Aires'),
    ('Lucía', 35, 'Rosario'),
    ('Pedro', 28, 'Córdoba')
""")
```

## SELECT