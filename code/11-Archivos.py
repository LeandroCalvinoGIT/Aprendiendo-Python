# ==================================================
# EJERCICIO 1 - CREAR Y ESCRIBIR ARCHIVO
# ==================================================
# Crear un archivo llamado "saludo.txt"
#
# El programa debe:
# - Abrir el archivo en modo escritura ("w")
# - Usar encoding="utf-8"
# - Escribir la frase:
#   "Hola, estoy aprendiendo archivos en Python"
# - El archivo debe cerrarse automáticamente
# - Mostrar por consola un mensaje de confirmación

try:
    with open("code/archivos/saludo.txt", "w", encoding="utf-8") as archivo_saludo:
        archivo_saludo.write("Hola, estoy aprendiendo archivos en Python")
except OSError as e:
    print(f"Error al intentar abrir el archivo:", e)
else:
    print("Manipulación de archivo completada correctamente!")

# ==================================================
# EJERCICIO 2 - LECTURA COMPLETA DE ARCHIVO
# ==================================================
# Abrir el archivo "saludo.txt"
#
# El programa debe:
# - Abrir el archivo en modo lectura ("r")
# - Leer todo el contenido usando .read()
# - Mostrar el contenido por consola
# - No usar close() explícitamente

try:
    with open("code/archivos/saludo.txt", "r", encoding="utf-8") as archivo:
        print(archivo.read())
except OSError as e:
    print(f"Error al intentar abrir el archivo:", e)


# ==================================================
# EJERCICIO 3 - AGREGAR CONTENIDO AL ARCHIVO
# ==================================================
# Trabajar con el archivo "saludo.txt"
#
# El programa debe:
# - Abrir el archivo en modo append ("a")
# - Agregar una nueva línea que diga:
#   "Esta es una nueva línea agregada"
# - Cerrar automáticamente el archivo
#
# Luego:
# - Abrir el archivo en modo lectura
# - Mostrar todo su contenido por consola

try:
    with open("code/archivos/saludo.txt", "a", encoding="utf-8") as archivo:
        archivo.write("\nEsta es una nueva línea agregada")
except OSError as e:
    print(f"Error al intentar abrir el archivo:", e)

try:
    with open("code/archivos/saludo.txt", "r", encoding="utf-8") as archivo:
        print(archivo.read())
except OSError as e:
    print(f"Error al intentar abrir el archivo:", e)

# ==================================================
# EJERCICIO 4 - CONTADOR DE LÍNEAS
# ==================================================
# Crear (o usar) un archivo llamado "datos.txt"
# que contenga varias líneas de texto
#
# El programa debe:
# - Abrir el archivo en modo lectura
# - Leer todas las líneas usando .readlines()
# - Mostrar:
#   * La cantidad total de líneas
#   * Cada línea numerada (Ej: "Línea 1: ...")
#
# Tip:
# - .readlines() devuelve una lista
# - Usar len() y un bucle for

try:
    # Abro en modo escritura/lectura
    with open("code/archivos/datos.txt", "w+", encoding="utf-8") as archivo:
        # Escribo el archivo
        archivo.write("Stranger Things\n")
        archivo.write("The Umbrella Academy\n")
        archivo.write("Sherlock Holmes\n")
        archivo.write("Fleabag\n")
        archivo.write("Gen V\n")
        # Devuelvo el puntero al inicio
        archivo.seek(0)
        # Guardo las lineas del archivo
        lineas = archivo.readlines()
except OSError as e:
    print(f"Error al intentar abrir el archivo:", e)
else:
    print("Manipulación de archivo completada correctamente!")

print("---------------------------")
print(f"Cantidad total de Líneas: {len(lineas)}")
indice = 1
for linea in lineas:
    print(f"Linea {indice}: {linea}")
    indice +=1
print("---------------------------")


# ==================================================
# EJERCICIO 5 - MANEJO DEL PUNTERO
# ==================================================
# Abrir un archivo de texto en modo lectura
#
# El programa debe:
# - Leer los primeros 10 caracteres del archivo
# - Mostrar esos caracteres
# - Mostrar la posición actual del puntero (tell)
# - Mover el puntero al inicio del archivo (seek)
# - Leer todo el contenido completo
# - Mostrar el contenido final por consola
#
# Importante:
# - Usar seek() y tell()
# - No usar close()

try:
    # Abro en lectura
    with open("code/archivos/datos.txt", "r", encoding="utf-8") as archivo:
        print(archivo.read(10))
        print(f"La posición actual del puntero es: {archivo.tell()}")
        archivo.seek(0)
        print(archivo.read())
except OSError as e:
    print(f"Error al intentar abrir el archivo:", e)
else:
    print("Manipulación de archivo completada correctamente!")