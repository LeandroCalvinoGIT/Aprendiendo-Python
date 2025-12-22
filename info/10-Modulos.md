En este archivo recopilo los modules y sus usos (usar help("modules"))

# MODULOS: 

Archivo que contiene funciones y variables utiles para otro

## IMPORT:
import modulo                   #Importa el modulo
import modulo as m              #Importa el modulo y lo renombra
from modulo import r            #Importa del modulo una variable o funcion
from modulo import *            #Importa TODO del modulo

modulo.funcion()
modulo.variable
print(m.variable)
print(r)

## NAMESPACE
Conjunto de todos los nombres definidos, se pueden ver haciendo:
print(dir(modulo))

Para que el codigo del modulo solo se ejecute cuando se use como programa principal, hay que agregar:
usar if __name__ = "__main__"
        main()

----------------------------------------------------------------------------------------------------------
## MÓDULO DE MÁTEMATICA: import math

math.pi --> valor de el número pi
math.e --> valor de el número e

math.sqrt()  --> raíz cuadrada de un número

math.ceil()  --> Redondea un número float para arriba
math.floor() --> Redondea un número float para abajo
----------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------
## MÓDULO DE TIEMPO: import time

El método time.sleep(x) hace que el programa espere x segundos
-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------
## MÓDULO RANDOM: import random

El método random.random() devuelve un float al azar entre \[\o,1\)
El método random.uniform(a,b) devuelve un float al azar entre [\a,b]
El método random.randint(a,b) devuelve un entero al azar del rango a-b
El método random.choice(coleccion) devuelve un elemento al azar de la coleccion
El método random.shuffle(coleccion) mezcla los elementos en una coleccion ordenada

EJ:

low = 1
high = 100
options = ("piedra", "papel", "tijera")
cartas = ["A", "1", "2", "3", "4", "5", "6", "7", "8","9", "10", "J", "Q", "K"]

#number = random.randint(low, high)
#number = random.random()
#option = random.choice(options)

random.shuffle(cartas)


print(cartas)

-----------------------------------------------------------------------------------------------------------

## MÓDULO STRING: import string

El método string.punctuation devuelve:          !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
El método string.digits devuelve:               0123456789
El método string.ascii_letters devuelve:        abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
El método string.ascii_lowercase devuelve:      abcdefghijklmnopqrstuvwxyz
El método string.ascii_uppercase devuelve:      ABCDEFGHIJKLMNOPQRSTUVWXYZ

### STRING METHODS:

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

El método "b".join("n") añade n a b

# PAQUETES

Directorio con módulos relacionados entre sí. Pueden ser enviados (distribuidos)

Para acceder a un modulo en otra carpeta:

from carpeta.archivo import m



