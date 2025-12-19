# BUCLES:

## KEYWORDS:
**break**        # sale del bucle
**continue**       # saltea una iteración
**pass**           # no hace nada

## WHILE: 

Ejecuta un bloque de código mientras que la condición se cumpla

    while condición:
        instrucción
    
## FOR: 

Ejecuta un bloque de código una cantidad de veces prefijada

    for variable in (iterable):
        instrucción

La función ***range(a,b,c)*** genera una lista de los numeros iniciando en a y terminando en b-1 con salto c
La función **reversed()** da vuelta el orden de una lista

## BUCLES ANIDADOS: Un bucle adentro de otro

EJ: for x in range(3):                      # imprime:
        for y in range(1,11):               # 1-2-3-4-5-6-7-8-9-10-/
            print(y, end="-")               # 1-2-3-4-5-6-7-8-9-10-/
        print("/")                          # 1-2-3-4-5-6-7-8-9-10-/

# STRING METHODS

## len()
La función len() devuelve un int con la cantidad de caracteres del string ingresado

    EJ: len("leandro") # devuelve 7

## .find

El método .find devuelve la posición de la primera instancia de un caracter

    EJ: variable = "Hola Mundo"
        variable.find("o") # devuelve 1 (H0, o1, l2, a3)

## .rfind

El método .rfind realizá lo mismo, pero buscando la última aparición

    EJ: variable = "Hola Mundo"
        variable.rfind("o") # devuelve 9 

En caso de no encontrar ninguna instancia del cáracter, devuelve -1

    EJ: variable = "Hola Mundo"
        variable.find("r") # devuelve -1


## .capitalize()
El método .capitalize() permite colocar el primer caracter del string en mayúscula

## .upper() y .lower()
El método .upper() convierte el string a todo mayúscula
El método .lower() convierte el string a todo minúscula

## .isdigit() y .isalpha()

El método .isdigit() devuelve true cuando el string esta conformado solo por digitos (0-9)
El método .isalpha() devuelve true cuando el string esta conformado solo por letras del alfabeto

## .count()

El método .count() cuenta cuantas veces aparece un caracter en el string y devuelve un int

    Ej: string = "12-23-34-45-56"
        string.count("-") # devuelve 4
        string.count("3") "devuelve 2

## .replace()

El método .replace( "a", "b") cambia todas las instacias del primer caracter(a) por el segundo(b)

    EJ: palabra = "whoooo"
        palabra.replace("o", "y") # devuelve "whyyyy"

## help(str)

La función help(str) da una lista de métodos útiles