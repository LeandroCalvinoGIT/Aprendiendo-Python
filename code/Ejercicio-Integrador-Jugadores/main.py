# ==================================================
# PROYECTO INTEGRADOR - SISTEMA DE GESTIÓN DE JUGADORES
# ==================================================
#
# OBJETIVO GENERAL:
# Crear un sistema que permita gestionar jugadores de un juego,
# guardarlos en un archivo y recuperarlos, aplicando TODOS los
# conceptos vistos hasta ahora.
#
# --------------------------------------------------
# TEMAS QUE DEBE INTEGRAR OBLIGATORIAMENTE:
# - Variables
# - Operadores
# - Condicionales
# - Bucles
# - Colecciones (listas y diccionarios)
# - Funciones
# - Excepciones (try / except / else)
# - Programación Orientada a Objetos (POO)
# - Métodos de strings (strip, split, lower, upper, isdigit, etc.)
# - Módulos (crear al menos un módulo propio)
# - Archivos (with as, read, write, append)
# --------------------------------------------------
#
# ==================================================
# PARTE 1 - CLASE JUGADOR (POO)
# ==================================================
#
# Crear una clase llamada Jugador
#
# La clase debe tener:
# - Atributos:
#   * nombre (str)
#   * nivel (int)
#   * vida (int)
#   * inventario (lista de strings)
#
# - Métodos:
#   * __init__
#   * mostrar_info() -> imprime todos los datos del jugador
#   * subir_nivel() -> aumenta el nivel en 1
#   * recibir_daño(cantidad) -> reduce la vida sin que baje de 0
#
# Validaciones:
# - nombre no puede estar vacío
# - nivel y vida deben ser enteros positivos
#
# Manejar errores con excepciones donde corresponda
#
# ==================================================
# PARTE 2 - FUNCIONES DE UTILIDAD (FUNCIONES + STRINGS)
# ==================================================
#
# Crear funciones que:
#
# 1) Soliciten datos al usuario:
#    - Nombre del jugador
#    - Nivel
#    - Vida
#    - Inventario separado por comas
#
# 2) Limpien los datos ingresados:
#    - strip()
#    - lower() o capitalize() para nombres
#    - split(",") para inventario
#
# 3) Validen:
#    - Que nivel y vida sean numéricos
#    - Que el inventario tenga al menos un item
#
# Si hay errores:
# - Mostrar mensajes claros
# - Evitar que el programa se rompa
#
# ==================================================
# PARTE 3 - COLECCIONES Y BUCLES
# ==================================================
#
# Crear una lista que almacene objetos Jugador
#
# Implementar un menú que se repita hasta que el usuario elija salir:
#
# 1 - Crear nuevo jugador
# 2 - Mostrar todos los jugadores
# 3 - Subir nivel a un jugador
# 4 - Guardar jugadores en archivo
# 5 - Cargar jugadores desde archivo
# 6 - Salir
#
# Usar bucles y condicionales para controlar el flujo
#
# ==================================================
# PARTE 4 - ARCHIVOS
# ==================================================
#
# Guardar los jugadores en un archivo de texto:
#
# - Nombre del archivo: jugadores.txt
# - Cada jugador en una línea
# - Formato sugerido:
#   nombre;nivel;vida;item1,item2,item3
#
# Requisitos:
# - Usar with open(...)
# - encoding="utf-8"
# - Manejar FileNotFoundError y OSError
#
# ==================================================
# PARTE 5 - CARGA DESDE ARCHIVO
# ==================================================
#
# Leer el archivo jugadores.txt
#
# - Parsear cada línea usando split(";") y split(",")
# - Crear objetos Jugador a partir de los datos
# - Agregarlos a la lista de jugadores
#
# Validar:
# - Que el archivo exista
# - Que los datos tengan el formato correcto
#
# ==================================================
# PARTE 6 - MÓDULOS
# ==================================================
#
# Separar el proyecto en al menos DOS archivos:
#
# - jugador.py -> clase Jugador
# - main.py -> lógica principal del programa
#
# Importar correctamente la clase Jugador
#
# ==================================================
# PARTE 7 - EXCEPCIONES
# ==================================================
#
# Usar try / except / else en:
# - Conversión de tipos
# - Lectura y escritura de archivos
# - Acceso a índices de listas
#
# No permitir que el programa se corte inesperadamente
#
# ==================================================
# DESAFÍOS OPCIONALES (NO OBLIGATORIOS)
# ==================================================
#
# - Ordenar jugadores por nivel
# - Buscar jugador por nombre
# - Calcular promedio de niveles
# - Usar __str__ en la clase Jugador
#
# ==================================================
# FIN DEL PROYECTO
# ==================================================
