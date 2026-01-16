# 01: Pide un número al usuario y cuenta desde 0 hasta ese número usando while.

""" numero = int(input("Ingresa el numero hasta el cual deseas contar: "))
contador = 0

while contador <= numero:
    print(contador)
    contador += 1 """

#02: Tabla de multiplicar: Pide un número y muestra su tabla de multiplicar del 1 al 10.

""" numero = int(input("Ingresa el numero del cual deseas cosaber su tabla: "))
multiplicadores = range(1,11,1)


print(f"---Tabla del {numero}----")

for multiplicador in multiplicadores:
    print(f"{numero} X {multiplicador} = {numero * multiplicador}")

print("-----------------------") """

#03: Pares e impares: Pedir 10 numero al usuario y contar cuantos son pares e impares

""" cant_pares = 0
cant_impares = 0

for number in range(1,11,1):
    numero = int(input("Ingresa un numero: "))
    if numero % 2 == 0:
        cant_pares += 1
    else:
        cant_impares += 1

print(f"Se ingresaron {cant_pares} numeros pares, y {cant_impares} numeros impares") """

#04: Adivinar el número 🎯 
# El programa tiene un número secreto (por ejemplo 7)
# El usuario intenta adivinarlo
# El bucle termina cuando acierta

""" numero_secreto = 6
numero_adivinado = 0

while numero_adivinado != numero_secreto:
    numero_adivinado = int(input("Adivina el número secreto!: "))
    if numero_adivinado != numero_secreto:
        print("NOP! volve a intentarlo: ")

print("Adivinaste! El número secreto era 6") """

#05: Números primos: Pide un número y di si es primo o no.

""" numero = int(input("Ingresa el numero para saber si es primo: "))
esPrimo = True

for divisor in range(2,numero,1):
    if numero % divisor == 0:
        print(f"El número {numero} es divisible por {divisor}")
        esPrimo = False

if esPrimo:
    print(f"El número {numero} es un número Primo :D")
else:
    print(f"El número {numero} NO es un número Primo :s") """

#06: Piramide de caracteres:

caracter = input("Ingresa un caracter!: ")



