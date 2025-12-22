# STRINGS

Python maneja los strings como una clase, por lo que tienen propiedades y métodos.

# STRING METHODS

## len()
La función len() devuelve un int con la cantidad de caracteres del string ingresado

    EJ: len("leandro") # devuelve 7

## .capitalize(), .upper() y .lower()
- El método .capitalize() permite colocar el primer caracter del string en mayúscula
- El método .upper() convierte el string a todo mayúscula
- El método .lower() convierte el string a todo minúscula

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

## .count()

El método .count() cuenta cuantas veces aparece un caracter en el string y devuelve un int

    Ej: string = "12-23-34-45-56"
        string.count("-") # devuelve 4
        string.count("3") "devuelve 2

## .isdigit(), .isalpha(), y .isalnum()

El método .isdigit() devuelve true cuando el string esta conformado solo por digitos (0-9)
El método .isalpha() devuelve true cuando el string esta conformado solo por letras del alfabeto
El método .isalnum() devuelve true cuando el string esta conformado solo por alphanumericos (diigitos y letras)

## .split()

El método .split() divide un string en partes y devuelve una lista de strings. Por defecti divide espacios, pero se puede introducir como parametro el caracter a separar, y el máximo de divisiones:
- texto.split(separador, maxsplit)
- 
Ejemmplos:

```python
# por defecto
texto = "Hola mundo desde python"
palabras = texto.split() 
print(palabras) # ["Hola", "mundo", "desde", "python"]

# con separador
datos = "10,20,30,40"
datosSperados = datos.split(",")
print(datosSperados)# ["10", "20", "30", "40"]

# con máximo:
palabras2 = texto.split(" ", 2) 
print(palabras2) # ["Hola", "mundo", "desde python"]
```

## .strip()

El método .strip() elimina espacios en blanco al inicio y al final del string.
Se puede pasar como parámetro un caracter en especifico para eliminar

Espacios en blanco incluye:
- espacios (" ")
- tabulaciones (\t)
- saltos de línea (\n)

### .lstrip() y .rstrip()

Ambos métodos tienen el mismo esfecto pero solo a izquierda/derecha.

Ejemplo: 
```python
# strip comun
texto = "     hola mundo           "
print(texto.strip()) # "hola mundo"

#lstrip y rstrip
print(texto.lstrip()) # "hola mundo        "
print(texto.rstrip()) # "        hola mundo"

#Con parametro
texto = "-------Hola mundo!------"
print(texto.strip("-")) # "hola mundo!"

```
## .replace()

El método .replace( "a", "b") cambia todas las instacias del primer caracter(a) por el segundo(b)

    EJ: palabra = "whoooo"
        palabra.replace("o", "y") # devuelve "whyyyy"

## help(str)

La función help(str) da una lista de métodos útiles