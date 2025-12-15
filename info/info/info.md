La función print() se utiliza para mostrar elementos por consola

EJ: print("Hola mundo!)

Agregando un segundo end="" parámetro se modifica el caracter final (por defecto es newline)

print("HOLA", end="x")  # imprime HOLAx

El # se usa para comentarios de una sola línea

Las comillas triples """ para comentar un bloque entero de código """

las variables se escriben usando la convención de snake_case

primer_variable = valor

se usa el = para asignar un valor a dicha variable

TIPOS DE DATOS:

Los tipos de datos básicos son los siguientes:
    Entero (int)            ej: 305
    Flotante (float)        ej: 203.43
    Cadena de texto(str)    ej: "Hola mundo!"   
    Booleano (bool)         ej: True False


La función type() devuelve el tipo de dato que contiene una variable cualquiera
La funcion isinstance(variable,tipo) devuelve un booleano si hay match

Ej: print(type(variable))

-----------------------------------------------------------------------------------------------------------
TYPECASTING:

Para pasar de un tipo de dato a otro se utilizan las funciones: int() , str() , bool() float()

Ej: edad = 20
    edad = float(edad)
    print(type(edad))   #esto va a devolver float

-----------------------------------------------------------------------------------------------------------
INPUT:

La función input() solicita al usuario que ingrese datos y los devuelve en forma de string

Ej:

nombre = input("Porfavor, ingrese su nombre)
print(f"Su nombre es: {nombre})

En el caso de querer recibir la información cómo dato numérico para poder operar con ella, es necesario realizar la conversión explícita del dato, de la siguiente forma:

edad = int(input("ingrese su edad: "))
edad += 1
print(f"el próximo año tendrá {edad} años")

-----------------------------------------------------------------------------------------------------------
ARITMETICA:

Los siguientes símbolos representan las siguientes operaciones:

= Asignar                   == Comparar
+ Suma                      += Incrementar  
- Resta                     -= Decrementar
* Multiplicación            *= Multiplicar
/ División                  /= Dividir
// División entera          
% Módulo (resto)
** Potenciación             **= Exponente

REDONDEO: La función round(valor, decimales) redondea un valor al entero(int) más cercano

    Ej:
    num1 = 3.14
    num2 = 3.68
    print(round(num1))  # va a devolver el entero 3
    print(round(num2))  # va a devolver el entero 4
    round(num1,1)       #va a devolver el número 3.1

VALOR ABSOLUTO: La función abs() devuelve el valor absoluto de un númer

    Ej:
    num = -23
    print(abs(num)) # va a devolver 23


POTENCIA: La función pow(base, exp) eleva la base al exponenete indicado y devuelve el resultado

    EJ: print(pow(2,5)) # va a devolver 32

MÁXIMO: La función max() devuelve el máximo de sus parámetros

MÍNIMO: La función min() devuelve el mínimo de sus parámetros

MÓDULO DE MÁTEMATICA: import math

math.pi --> valor de el número pi
math.e --> valor de el número e

math.sqrt()  --> raíz cuadrada de un número

math.ceil()  --> Redondea un número float para arriba
math.floor() --> Redondea un número float para abajo

-----------------------------------------------------------------------------------------------------------
CONDICIONALES:

IF: Se usa para ejecutar un bloque de código solo si se cumple una condición

Estructura:

if condición:
    instrucción
elif
    instrucción
else
    instrucción

OPERADORES LÓGICOS: OR, AND, NOT

EXPRESIÓN CONDICIONAL: X if condición else Y
EJ: print("Cumple" if true else "No cumple")

-----------------------------------------------------------------------------------------------------------
STRING METHODS:

La función len() devuelve un int con la cantidad de caracteres del string ingresado

    EJ: len("leandro") # devuelve 7

El método .find devuelve la posición de la primera instancia de un caracter

    EJ: variable = "Hola Mundo"
        variable.find("o") # devuelve 1 (H0, o1, l2, a3)

El método .rfind realizá lo mismo, pero buscando la última aparición

    EJ: variable = "Hola Mundo"
        variable.rfind("o") # devuelve 9 

En caso de no encontrar ninguna instancia del cáracter, devuelve -1

    EJ: variable = "Hola Mundo"
        variable.find("r") # devuelve -1

El método .capitalize() permite colocar el primer caracter del string en mayúscula

El método .upper() convierte el string a todo mayúscula
El método .lower() convierte el string a todo minúscula

El método .isdigit() devuelve true cuando el string esta conformado solo por digitos (0-9)
El método .isalpha() devuelve true cuando el string esta conformado solo por letras del alfabeto

El método .count() cuenta cuantas veces aparece un caracter en el string y devuelve un int

    Ej: string = "12-23-34-45-56"
        string.count("-") # devuelve 4
        string.count("3") "devuelve 2

El método .replace( "a", "b") cambia todas las instacias del primer caracter(a) por el segundo(b)

    EJ: palabra = "whoooo"
        palabra.replace("o", "y") # devuelve "whyyyy"

La función help(str) da una lista de métodos útiles

-----------------------------------------------------------------------------------------------------------
INDEXACIÓN:

Agregando [] al final de un string, se puede acceder a parte de sus caracteres mediante su indice

        [start : end : step]        start incluye, end no

numero = "1234-5678-9012-3456"

print(numero[0])    # imprime 1
print(numero[4])    # imprime -

print(numero[0:4])  # imprime 1234, es lo mismo que poner numero[:4]
print(numero[5:9])  # imprime 5678

print(numero[5:])   # imprime 5678-9012-3456, es lo mismo que poner numero[5:last]
print(numero[-1])   # imprime 6, es lo mismo que poner numero[18]
 
print(numero[::2])  # imprime 13-6891-46 (cada dos números)
print(numero[::3])  # imprime 146-136   (cada tres números)

print(numero[::-1]) # imprime el string dado vuelta, 6543-2109-8765-4321
-----------------------------------------------------------------------------------------------------------

ESPECIFICADORES DE FORMATO:

{value:flags}  formatea el valor de acuerdo a los flags asignados:

1) .(numero)f = Redondea a (numero) decimales (punto fijo)
2) :(numero)  = Asigna (numero) cantidad de espacios
3) :0(numero) = Asigna (numero) cantidad de espacios con ceros al principio
4) :<         = Justifica texto a la izquierda
4) :>         = Justifica texto a la derecha
5) :^         = Justifica texto al centro
6) :+         = Usa signo + para vaolores positivos
7) :=         = Pone el signo a la izquierda
8) :          = Inserta un espacio antes de numeros positivos
9) :,         = Separa con comas las unidades

EJ: numero1 = 3000.453  numero2 = -98765.34

print(f"El precio es: ${p1:+,.2f}")
print(f"El precio es: ${p2:^20}")

El precio es: $+3,000.45
El precio es: $     -98765.34  
-----------------------------------------------------------------------------------------------------------

BUCLES:

break          # sale del bucle
continue       # saltea una iteración
pass           # no hace nada


WHILE: Ejecuta un bloque de código mientras que la condición se cumpla

    while condición:
        instrucción
    
FOR: Ejecuta un bloque de código una cantidad de veces prefijada

    for variable in (iterable):
        instrucción

La función range(a,b,c) genera una lista de los numeros iniciando en a y terminando en b-1 con salto c
La función reversed() da vuelta el orden de una lista

BUCLES ANIDADOS: Un bucle adentro de otro

EJ: for x in range(3):                      # imprime:
        for y in range(1,11):               # 1-2-3-4-5-6-7-8-9-10-/
            print(y, end="-")               # 1-2-3-4-5-6-7-8-9-10-/
        print("/")                          # 1-2-3-4-5-6-7-8-9-10-/
-----------------------------------------------------------------------------------------------------------
TIME:
import time

El método time.sleep(x) hace que el programa espere x segundos
-----------------------------------------------------------------------------------------------------------

COLECCIONES: Variables que almacenan varios valores

List  = []   ordenada y modificable, puede haber duplicados
Set   = {}   desordenada e inmutable, no duplicados, se puede añadir/quitar
Tuple = ()   ordenada e inmodificable, puede haber duplicados, más rápida.

len(coleccion)              # devuelve la cant de elementos

IN: devuelve un booleano si el elemento está en la colección
    ej:elemento1 in lista      # devuelve True


LISTAS: 
lista = [elemento1, elemento2, elemento3]

print(lista[0])         # imprime el primer elemento
len(lista)              # devuelve la cant de elementos

MÉTODOS EN LISTAS:

El método .append(elemento) añade un elemento al final de la lista
El método .remove(elemento) elimina un elemento de la lista
El método .insert(index, element) inserta un elemento en la posición indicada
El método .sort() ordena la lista en orden alfabético
El método .reverse() Invierte el orden de la lista
El método .clear() elimina todos los elementos de la lista
El método .index(elemento) devuelve el index del elemento
El método .count(elemento) devuelve la cant de veces que dicho elemento de encuentra en la lista


SET:
set = {elemento1, elemento3, elemento4, elemento2}

print(set)  # imprime sin un orden determinado

MÉTODOS DE SET:

El método .add(elemento) añade un elemento al conjunto
El método .remove(elemento) elimina un el elemento del conjunto
El método .pop() elimina un elemento al azar
El método .clear() elimina todos los elementos

TUPLAS:
tuple = (elemento1, elemento2, elemento3)

MÉTODOS DE TUPLA:

El método .index(elemento) devuelve la posición de un elemento
El método .count(elemento) devuelve la cantidad de el elemento en la tupla

COLECCIONES 2D:

Es una coleccion compuesta por otras colecciones
EJ: colecciones = [coleccion1, coleccion2, coleccion3]

comidas = [ ["manzana", "banana", "pera"],
            ["carne", "pollo", "pescado"],
            ["helado", "chocolate", "flan"]]

para iterar:

for coleccion in colecciones:
    for elemento in coleccion:
        print(elemento, end=" ")
    print()

-----------------------------------------------------------------------------------------------------------

DICCIONARIOS: Colección de pares {key:value} ordenados y modificables, no repetidos

ej:     Capitals = {"Argentina":"CABA,
                    "USA":"Washington D.C.",
                    "Peru":"Lima"}

MÉTODOS DE DICCIONARIOS:

El método .get(key) devuelve el value asociado
El método .update({key:value}) agrega un elemento al diccionario
El método .pop(key) elimina el par asociado
El método .popitem() elimina el último elemento añadido al diccionario
El método .clear() elimina todos los elementos del diccionario
El método .keys() devuelve un objeto con todas las keys del diccionario
El método .values() devuelve un objeto con todas los values del diccionario
El método .items() devuelve un objeto con todos los pares del diccionario

iteracion:

keys:   for key in diccionario.keys():
            print(key)

values:   for value in diccionario.values():
            print(value)  

items:  for key,value in diccionario.items():
            print(f"{key}:{value}")

