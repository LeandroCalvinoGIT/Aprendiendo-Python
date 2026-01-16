# BDD relacional

BDD: Conjuntos de datos de un mismo contexto almacenados sistematicamente para su posterior uso

Relacional: Se modelan clases y entidades como tablas con registros (filas) y columnas (atributos)

Tabla: sirve para ordenar los valores segun los atributos definidos. Representan entidades.

Atributo: Hecho simple que define a una entidad.

Registros: n-uplas que agrupan los valores de atributos asignados a la instancia del objeto

Clave primaria: ID que sirve para identificar unicamente a una tupla.
Clave foranea: En una tabla distinta, se coloca como atributa la clave primaria de la tabla original.

# SQL

Lenguaje usado en BDD para manipulacion ded atos.

- DDL: Definicion y modificar objetos
- DML: consultar datos
- DCL: Controlar y gestionar acceso

## CONSTRAINTS
son restricciones que se utilizan para limitar el tipo de
dato que puede recibir una columna de una tabla.
Se pueden definir cuando creamos la tabla (CREATE TABLE) o
posteriormente con la sentencia ALTER TABLE.

## SENTENCIAS BASICAS

### DDL

CREATE: crea objetos, bases, tablas, etc. 

EJ:
```sql
 CREATE OR REPLACE TABLE nombre (
    atributos tipo caracteristicas
)
```

ALTER: modifcar la definicion de un objeto:
- Agregar o borrar columnas
- Cambiar tipo de dato de una columna
- Establecer valor por defecto
- Modificar una tabla con nueva clave/borrar clave

DROP: Permite eliminar basese de datos, tablas, columnas

EJ:
```sql
ALTER TABLE nombre_tabla
ADD COLUMN nombre tipo --AGREGAR COLUMNA
DROP COLUMN nombre tipo-- BORRAR COLUMNA

ALTER COLUMN nombre nurvo_tipo -- CAMBIAR TIPO DE DATO DE UNA COLUMNA

-- ESTABLECER UN VALOR POR DEFECTO
ALTER TABLE nombre_tabla ADD CONSTRAINT nombre_valor_por_defecto
DEFAULT valor FOR nombre_column

```