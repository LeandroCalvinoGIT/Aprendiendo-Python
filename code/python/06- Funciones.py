# EJERCICIO 1 - VALIDACION BASICA
# -------------------------------

# Crea una funcion llamada es_mayor_de_edad
# - Recibe una edad
# - Retorna True si la edad es mayor o igual a 18
# - Retorna False en caso contrario

def es_mayor_de_edad(edad):
    return edad >=18
        

# -------------------------------
# EJERCICIO 2 - FUNCION CON LISTA
# -------------------------------

# Crea una funcion llamada calcular_promedio
# - Recibe una lista de numeros
# - Retorna el promedio
# - Asumi que la lista NO esta vacia

""" def calcular_promedio(notas):
    #inicializa promedio
    promedio = 0

    #suma cada nota de la lista
    for nota in notas:
        promedio += nota

    #divide el total por la cantidad de notas
    promedio /= len(notas)

    #devuelve el promedio calculado
    return promedio """

# -------------------------------
# EJERCICIO 3 - FUNCION QUE PROCESA DATOS
# -------------------------------

# Crea una funcion llamada filtrar_pares
# - Recibe una lista de numeros
# - Retorna una nueva lista solo con los numeros pares

def es_par(numero):
    return numero % 2 == 0

def filtrar_pares(numeros):

    pares = []

    for numero in numeros:
        if es_par(numero):
            pares.append(numero)
    
    return pares

# -------------------------------
# EJERCICIO 4 - FUNCION + CONTROL DE FLUJO
# -------------------------------

# Crea una funcion llamada dividir
# - Recibe dos numeros
# - Si el segundo numero es 0, retorna None
# - Si no, retorna el resultado de la division

def dividir(dividendo, divisor):
    if divisor == 0:
        return None
    else:
        return dividendo / divisor

# ----------------------------------------------------------
# EJERCICIO 1 - GESTION DE NOTAS
# ----------------------------------------------------------

# Crear un programa que permita gestionar notas de estudiantes.
#
# Requisitos:
# - El programa debe pedir al usuario ingresar notas (numeros).
# - El usuario puede ingresar tantas notas como quiera.
# - El ingreso termina cuando el usuario escribe "fin".
#
# El programa debe:
# 1) Guardar las notas en una lista.
# 2) Validar que cada nota sea un numero entre 0 y 10.
# 3) Ignorar (no guardar) valores invalidos.
# 4) Usar funciones para:
#    - validar una nota
#    - calcular el promedio
# 5) Al finalizar, mostrar:
#    - todas las notas ingresadas
#    - el promedio
#    - la nota mas alta
#    - la nota mas baja
#
# Restricciones:
# - No usar librerias externas.
# - No mezclar print con logica dentro de las funciones.
#
# Pistas:
# - Vas a necesitar un while
# - Usa funciones para separar responsabilidades

# FUNCIONES
def nota_es_valida(nota):
    if not nota.isdigit():
        return False
    nota = int(nota)
    return  0 <= nota <= 10

def calcular_promedio(notas):
    promedio = 0

    for nota in notas:
        promedio += nota

    promedio /= len(notas)

    return promedio

def nota_mas_alta(notas):
    nota_mas_alta = notas[0]
    for nota in notas:
        if nota > nota_mas_alta:
            nota_mas_alta = nota
    return nota_mas_alta

def nota_mas_baja(notas):
    nota_mas_baja = notas[0]
    for nota in notas:
        if nota < nota_mas_baja:
            nota_mas_baja = nota
    return nota_mas_baja

# INICIALIZACIONES
notas = []
nota = ""

# INPUT

while nota != "fin":
    nota = input("Ingresa una nota (fin para terminar): ")
    if nota_es_valida(nota):
        notas.append(int(nota))
    elif nota != "fin":
        print("Nota inválida! intenta de nuevo")
    else:
        print("Finalizado el ingreso de notas")

# OUTPUT
if len(notas) == 0:
    print("No se ingresaron notas :/")
else:
    print("-------Resumen de notas---------")
    print(f"Notas ingresadas: {notas}")
    print(f"Promedio total: {calcular_promedio(notas)}")
    print(f"Nota más alta: {nota_mas_alta(notas)}")
    print(f"Nota más baja: {nota_mas_baja(notas)}")
    print("----------------------------------")

# ----------------------------------------------------------
# EJERCICIO 2 - SISTEMA DE USUARIOS
# ----------------------------------------------------------

# Crear un sistema simple de usuarios.
#
# El programa debe:
# - Pedir al usuario que ingrese nombres de usuario.
# - Cada usuario debe guardarse como un diccionario con:
#   * nombre
#   * edad
#   * activo (True / False)
# - Todos los usuarios deben almacenarse en una lista.
#
# Reglas:
# 1) La edad debe ser un numero entero positivo.
# 2) Un usuario es "activo" si su edad es mayor o igual a 18.
# 3) El ingreso de usuarios termina cuando el nombre sea "salir".
#
# El programa debe usar funciones para:
# - validar edad
# - crear un usuario
# - mostrar usuarios activos
#
# Al finalizar, mostrar:
# - cantidad total de usuarios
# - lista de nombres de usuarios activos
# - lista de nombres de usuarios inactivos
#
# Restricciones:
# - No usar clases.
# - No usar librerias externas.
#

def edadEsValida(edad):
    if not edad.isdigit():
        return False
    edad = int(edad)
    return edad >= 0

def estaActivo(edad):
    return edad >= 18

def crearUsuario(nombre, edad):
    usuario = {
        "nombre": nombre,
        "edad"  : edad,
        "activo": estaActivo(edad)
    }
    return usuario

def filtrarUsuarios(usuarios, criterio):
    usuarios_filtrados = []

    #lista de usuarios activos
    if criterio == "activo":
        for usuario in usuarios:
            if usuario.get("activo"):
                usuarios_filtrados.append(usuario)
    elif criterio == "inactivo":
        for usuario in usuarios:
            if not usuario.get("activo"):
                usuarios_filtrados.append(usuario)
    else:
        print("criterio ingresado inválido")
    
    return usuarios_filtrados

def filtrarNombres(usuarios):
    nombres = []
    for usuario in usuarios:
        nombres.append(usuario.get("nombre"))
    return nombres

def mostrarUsuariosActivos(usuarios):
    if len(usuarios) == 0:
        print("No hay usuarios activos")
    else:
        usuarios_activos = filtrarUsuarios(usuarios, "activo")
        print(f"Los usuarios activos son: {usuarios_activos}")

usuarios = []
nombre = ""

while nombre != "salir":

    nombre  =    input("Ingresa el nombre del usuario: ")

    if nombre == "salir":
        print("Finalizo el ingreso de usuarios")
        break
    
    edad    =    input("Ingresa la edad del usuario en años: ")

    if not edadEsValida(edad):
        print("Edad ingresada inválida, vuelva a intentarlo")
        continue
    
    usuarios.append(crearUsuario(nombre, int(edad)))

usuarios_activos = filtrarUsuarios(usuarios, "activo")
usuarios_inactivos = filtrarUsuarios(usuarios, "inactivo")

# OUTPUT
print("-------Resumen de usuarios---------")
print(f"La cantidad total de usuarios ingresados es: {len(usuarios)}")
print(f"Los usuarios activos son: {filtrarNombres(usuarios_activos)}")
print(f"Los usuarios inactivos son: {filtrarNombres(usuarios_inactivos)}")
print("----------------------------------")

# ==========================================================
# FIN DE LOS EJERCICIOS
# ==========================================================