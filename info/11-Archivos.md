# Archivos

El objetivo es la persistencia de datos:

- Archivos externos
- Bases de datos (más adelante - BBDD)

En python se usa el **Módulo io** de la biblioteca estandar de python, y se manejan los archivos como objetos.

from io import open

## TIPOS DE ARCHIVOS

- Texto Plano
- Binario
- Raw

## FASES DE GUARDADO DE INFORMACIÓN

1. Creación
2. Apertura
3. Manipulación
4. Cierre

## MODOS DE APERTURA

- **r** → lectura (read)
  - Abre un archivo **existente** para lectura
  - ❌ Error si el archivo no existe → `FileNotFoundError`
  - ❌ No permite escribir
  - 📍 El puntero inicia al comienzo

- **w** → escritura (write)
  - Crea el archivo si no existe
  - ⚠️ borra todo el contenido si existe
  - ❌ No permite leer

- **a** → agregar al final (append)
  - Crea el archivo si no existe
  - Escribe siempre al final
  - ❌ No pisa el contenido existente
  - 📍 El puntero inicia al final

- **x** → creación exclusiva
  - Crea el archivo solo si no existe
  - ❌ Error si ya existe → FileExistsError
  - Útil para evitar sobrescrituras accidentales

- **r+** → lectura y escritura
  - ❌ Error si el archivo no existe
  - No borra el contenido
  - Lee y escribe desde la posición actual del puntero

- **w+** → lectura y escritura
  - Crea el archivo si no existe
  - ⚠️ Borra todo el contenido existente
  - Permite leer y escribir
  
- **a+** → agregar y lectura
  - Crea el archivo si no existe
  - Agrega contenido al final
  - Para leer, se debe mover el puntero con seek()


- **t** → modo texto (default)
- 
- **b** → modo binario (bytes)
  - "rb+" — Lectura y escritura binaria
  - "wb+" — Escritura y lectura binaria (borra contenido)
  - "ab+" — Agregar y lectura binaria


## MÉTODOS, ATRIBUTOS Y FUNCIONES DE ARCHIVOS

### open(ruta, modo, codificacion)

La función open(ruta, modo, encoding=codificacion) abre el archivo de la ruta, en el modo indicado, y con la codificacion indicada

### .write(a)

El método .write(a) sobreescrbe a en el archivo, y devuelve la cantidad de caracteres escritos.

### .writelines(lineas)

El método .writelines(lineas) escribe el contenido en el archivo en cada linea correspondiente a la lista.
Si se usa con el indice: .writelines(lineas[n]) escribirá el item n en la linea n
### .read(a)

El método .read(a) lee el contenido archivo hasta el caracter a

### .readlines()

El método .readlines() lee el contenido archivo linea a linea y lo almacena en una lista.

### .seek(a)

El método .seek(a) mueve el puntero dentro del archivo al caracter a

### .tell()

El método .seek(a) devuelve el indice del puntero dentro del archivo.

### .close()

El método .close() cierra el archivo

### .closed

El atributo .closed es un booleano que indica si el archivo está cerrado.

## With .. as --

Usando las keywords **with - as** y la siguiente estructura, se logra que el archivo se cierre automaticamente

```python
with open("archivo.md", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    archivo.seek(0)
    print(archivo.read())
    # No hace falta el close
print(lineas)
```

Es importante que el scope de with no limita las variables definidas dentro del mismo, por lo que lineas seguirá existiendo fuera de el

## PUNTERO

Al manipular archivos se utiliza un puntero para moverse dentro del mismo. Al abrirlo por ptimera vez, por defecto se situa al inicio.

## EXCEPCIONES:

- FileNotFoundError: Archivo o ruta no existe (al leer)
- PermissionError: No se cuenta con permiso para acceder al archivo
- IsADirectoryError: Se intento acceder a una carpeta como archivo
- FileExistsError: El archivo ya existe (usando 'x')
- UnsupportedOperation: Se intento realizar una operacion invalida para el modo en el que se abrio el file
- UnicodeDecodeError: Si se intenta leer en una codificacion invalida para el archivo
- UnicodeEncodeError: Si se intenta escribir con caracteres inexistentes en una codificación
- OSError: Error general

### CÓDIGO:
```python
try:
    with open("code/archivos/saludo.txt", "w", encoding="utf-8") as archivo_saludo:
        archivo_saludo.write("Hola, estoy aprendiendo archivos en Python")
    print("El archivo se escribió correctamente")
except OSError as e:
    print(f"Error al intentar abrir el archivo:", e)
    # Muestra el error que sucedio al abrir el archivo
```

## ESTRUCTURA DE CÓDIGO:

```python
from io import open

# Crear y escribir Archivo

archivo_texto = open("archivo.txt", "w", encoding="utf-8")

frase = "Estoy aprendiendo a usar archivos \n :D"

archivo_texto.write(frase)

archivo_texto.close()

# Leer archivo

archivo_texto = open("archivo.txt", "r")

#texto = archivo_texto.read()
lineas_texto = archivo_texto.readlines()

print(lineas_texto)

archivo_texto.close()

# Agregar contenido al archivo

archivo_texto = open("archivo.txt", "a")

archivo_texto.write("\n Soy una nueva linea")

archivo_texto.close()

# Mover puntero dentro del archivo

archivo_texto = open("archivo.txt", "r")

print(archivo_texto.read(11)) #imprime hasta la posicion 11)

archivo_texto.seek(0) # Mueve el puntero al inicio del archivo

archivo_texto.seek(len(archivo_texto.read())/2) # Mueve el puntero a la mitad del archivo

print(archivo_texto.tell()) # Imprime posición del puntero

archivo_texto.seek(11) # Mueve el puntero a la posicion 11

print(archivo_texto.read()) # Imprime a partir de la posicion [11

archivo_texto.close()
```