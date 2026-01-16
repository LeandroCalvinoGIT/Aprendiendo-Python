# ==========================================================
# EJERCICIOS PYTHON - MANEJO DE ERRORES
# DIA 4 - TRY / EXCEPT / ELSE / FINALLY / RAISE
# ==========================================================


# ----------------------------------------------------------
# EJERCICIOS SIMPLES
# ----------------------------------------------------------

# -------------------------------
# EJERCICIO 1 - DIVISION SEGURA
# -------------------------------

# Crea una funcion llamada dividir_seguro
# - Pide dos numeros al usuario
# - Retorna el resultado de la division
# - Maneja:
#   * ValueError (si el usuario no ingresa numeros)
#   * ZeroDivisionError (si divide por 0)
# - Usa finally para mostrar: "Operacion finalizada"

def dividir_seguro():
    try:
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo numero: "))
        return num1/num2
    except ValueError:
        print("Numeros ingresados inválidos")
        return "Error en los número ingresados"
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        return "Error matemático"
    finally:
        print("Operación finalizada")

# -------------------------------
# EJERCICIO 2 - VALIDAR ENTERO
# -------------------------------

# Crea una funcion llamada pedir_entero
# - Pide un numero al usuario
# - Retorna el numero como int
# - Si el usuario ingresa algo invalido, muestra un mensaje
# - El programa NO debe romperse

def pedir_entero():
    numero = input("Ingresa un número entero: ")

    try:
        return int(numero)
    except ValueError:
        print("Datos ingresados invalidos")
        return None


# -------------------------------
# EJERCICIO 3 - USO DE ELSE
# -------------------------------

# Crea una funcion llamada calcular_cuadrado
# - Pide un numero al usuario
# - Usa try / except
# - Si NO ocurre ningun error:
#   * Calcula el cuadrado del numero
#   * Usa else para mostrar el resultado

def calcular_cuadrado():
    try:
        numero = int(input("Ingresa un número: "))
    except:
        print("Ocurrió un error")
    else:
        print(f"El cuadrado del número es: {numero ** 2}")

# -------------------------------
# EJERCICIO 4 - CAPTURAR VARIOS ERRORES
# -------------------------------

# Crea una funcion llamada convertir_a_entero
# - Recibe un valor
# - Intenta convertirlo a int
# - Maneja ValueError y TypeError
# - Retorna None si ocurre un error

def convertir_a_entero(valor):

    try:
        numero = int(valor)
    except ValueError:
        print("El valor ingresado no es capaz de ser convertido a un número entero")
        return None
    except TypeError:
        print("Error en el tipo de valor recibido")
        return None
    else:
        return numero
    finally:
        print("finalizó la conversión")


# -------------------------------
# EJERCICIO 5 - RAISE SIMPLE
# -------------------------------

# Crea una funcion llamada validar_edad
# - Recibe una edad
# - Si la edad es negativa, lanza una excepcion con raise
# - Si la edad es valida, retorna True

def validar_edad(edad):
    if edad < 0:
        raise ValueError("No se permiten edades Negativas")
    else:
        return True

# ----------------------------------------------------------
# EJERCICIOS COMPLEJOS E INTEGRADORES
# ----------------------------------------------------------

# -------------------------------
# EJERCICIO 6 - PROMEDIO SEGURO
# -------------------------------

# Crear un programa que:
# - Pida al usuario ingresar numeros uno por uno
# - El ingreso termina cuando el usuario escribe "fin"
#
# El programa debe:
# - Guardar los numeros en una lista
# - Ignorar entradas invalidas usando try / except
# - NO romperse nunca
#
# Al finalizar:
# - Mostrar la lista de numeros
# - Calcular el promedio
# - Manejar el error de division por cero si la lista esta vacia

# Pistas:
# - Usa un while
# - Usa funciones
# - Usa try / except donde realmente haga falta

def calcular_promedio(numeros):
    promedio = 0
    for numero in numeros:
        promedio += numero
    
    try:
        promedio /= len(numeros)
    except ZeroDivisionError:
        print("No hay numeros en la lista, no es posible calcular el promedio")
        return None
    else:
        return promedio
    finally:
        print("Calculo del promedio finalizado")

print(type("hjola"))
numeros = []
numero = ""

while numero != "fin":
    numero = input("Ingresa el primer numero: ")
    if numero == "fin":
        break
    try:
        numero = int(numero)
    except ValueError:
        print("Valor ingresado invalido, vuelva a intentarlo: ")
    else:
        numeros.append(numero)

promedio = calcular_promedio(numeros)

print("----------PROMEDIO-------------")
print(f"Números ingresados: {numeros}")
if promedio != None:
    print(f"Promedio total: {promedio}")

# -------------------------------
# EJERCICIO 7 - SISTEMA DE EDADES ROBUSTO
# -------------------------------

# Crear un programa que:
# - Pida al usuario ingresar edades
# - El ingreso termina cuando el usuario escribe "salir"
#
# Reglas:
# - Si la edad es negativa, usar raise
# - Si la edad no es un numero, capturar la excepcion
#
# El programa debe:
# - Guardar las edades validas en una lista
# - Mostrar cuantas edades validas se ingresaron
# - Mostrar el promedio de edades
# - El programa NO debe romperse nunca

edades = []
edad = ""

while edad != "salir":
    edad  =    input("Ingresa una edad: ")
    
    if edad != "salir":
        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError("La edad ingresada no puede ser negativa")
        except ValueError:
            print("Valor ingresado invalido, vuelva a intentarlo: ")
        else:
            edades.append(edad)

promedio_edades = calcular_promedio(edades)
# OUTPUT
print("-------Resumen de Edades---------")
print(f"Edades ingresadas: {edades}")
print(f"La cantidad total de edades ingresadas es: {len(edades)}")
if promedio_edades is not None:
    print(f"El promedio de edades es: {promedio_edades}")
print("----------------------------------")


# ==========================================================
# FIN DE LOS EJERCICIOS
# ==========================================================
