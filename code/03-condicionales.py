#01: Pide un número al usuario e indica si es positivo, negativo o cero.

""" numero = float(input("Ingresa un numero: "))

if numero > 0:
    print("El número ingresado es positivo")
elif numero < 0:
    print("El número ingresado es negativo")
else:
    print("El número ingresado es 0") """

#02: Pide un número entero y muestra si es par o impar.

""" numero = int(input("Ingresa un numero: "))

numeroEsPar = numero % 2 == 0

if numeroEsPar:
    print(f"{numero} es par!")
else:
    print(f"{numero} es impar!") """

#03: Pide la edad de una persona e indica si es mayor de edad (18 o más) o menor de edad.

""" edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Sos mayor de edad!")
else:
    print("Sos menor de edad!")"""

#04: Pide dos números y muestra cuál es el mayor o si son iguales.

""" num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

if num1 > num2:
    print(f"El primer numero ({num1}) es mayor que el segundo ({num2})")
elif num1 < num2:
    print(f"El primer numero ({num1}) es menor que el segundo ({num2})")
else:
    print(f"El primer numero ({num1}) y el segundo numero ({num2}) son iguales") """

#05: Pide el total de una compra. Si es mayor a 100, aplica un 10% de descuento. 
# Si no, no hay descuento.
# Muestra el total a pagar.

""" total = float(input("Ingrese el total de la compra: "))

if total > 100:
    total-= total*0.1

print(f"El precio a pagar es de: ${total}") """

#06: Dia de la semana
# Pide un número del 1 al 7 y muestra el día correspondiente (1 = Lunes, 7 = Domingo).
# Si el número no es válido, muestra un mensaje de error.

""" numero = int(input("Ingresa un numero: "))

match numero:
    case 1:
        print("Es Lunes :C")
    case 2:
        print("Es Martes :(")
    case 3:
        print("Es Miércoles :|")
    case 4:
        print("Es Jueves :/")
    case 5:
        print("Es Viernes! :D")
    case 1:
        print("Es Sábado XD")
    case 1:
        print("Es Domingo :0")
    case _:
        print("Numero invalido") """

#07: Registrarse en la universidad!
# Pedir al usuario su edad, si la misma está entre 18 y 80 puede inscribirse, de lo contrario no 
# En segundo lugar consultar si el usuario termino estudios secundarios

""" print("Bienvenido al proceso de registro universitario!")

edad = int(input("Ingresa tu edad: "))

if edad >= 18 and edad <=80:
    if input("Termino sus estudios secundarios? (SI/NO): ") == "SI":
        print("Puede inscribirse! :D")
    else:
        print("Deberá terminar sus estudios secundarios antes de inscribirse")
else:
    print("No se puede registrar a la universidad (Debes tener entre 18 y 80 años)") """

#08: Calculadora de liquidación parte 2:

#Indemnizacion: Se le suma a la liquidacion: Es un sueldo bruto por año trabajado. 
# A pártir del año, y 3 meses, se cuenta como 2 años.
""" 
dias_del_mes = 30

salario_bruto = float(input("Ingrese el valor del salario bruto: "))
dias_trabajados = int(input("Ingrese la cantidad de dias trabajados este mes: "))
meses_trabajados = int(input("Ingrese la cantidad de meses trabajados: "))
sigueEmpleado = input("El empleado fue desvinculado? (SI/NO): ") == "NO"

liquidacion_base = (salario_bruto / dias_del_mes) * dias_trabajados

anios_trabajados = meses_trabajados // 12

if meses_trabajados % 12 > 3:
    anios_trabajados+= 1

indemnizacion = anios_trabajados * salario_bruto
liquidacion_final = liquidacion_base + indemnizacion

if sigueEmpleado:
    print(f"El salario total es de: ${liquidacion_base}")
else:
    print(f"La liquidacion final es de: ${liquidacion_final}")"""

