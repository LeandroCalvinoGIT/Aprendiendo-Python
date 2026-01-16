# ITERABLES: 

Objetos/colecciones que pueden devolver sus elementos uno a la vez, pudiendo ser iterados en un loop

Son iterables: 
- Listas
- Tuplas
- sets
- Diccionarios
- Strings

EJ:
```python
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {"apple", "orange", "banana", "coconut"}
my_name = "Bro Code"
my_dictionary = {'A': 1, 'B': 2, 'C': 3}

for item in my_coleccion:
    print(item)

DICTIONARIES
for key in my_dictionary:
    print(key)

for value in my_dictionary.values():
    print(value)

for key, value in my_dictionary.items():
    print(f"{key} = {value}")

```
# LISTAS COMPRIMIDAS: [expression for value in iterable if condition]

Sirve para simplificar el modo de crear listas y mejorar la legibilidad

EJ;

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

fruits = ["apple", "orange", "banana", "coconut"]
uppercase_words = [fruit.upper() for fruit in fruits]
fruit_first_chars = [fruit[0] for fruit in fruits]          

con condicion:

numeros = [-1, -2, -3, 4, -5, -6, 16]

mitad = [ x / 2 for x in numeros if numero%2 == 0]

# GENERADORES

Estructuras que extraen valores de una funcion y se almacenan en objetos iterables.
Al llamar a la funcion, se genera un valor y se almacena dentro del iterable, y cada llamada 
genera un nuevo valor dentro del iterable.

## Utilidad:
- Más eficientes que las funciones tradicionales
- Útiles con listas de valores infinitos
- Para ciertos contextos, es mejor que devuelva de a uno (lazy evaluation)

## Sintaxis:

Se utiliza la palabra reservada **yield**

```python
#Funcion normal:
def generaPares(limite):
    num = 1
    milista = []

    while num < limite:
        milista.append(num*2)
        num += 1

    return milista

print(generaPares(10))

#Funcion Generadora
def generadorPares(limite):
    num = 1

    while num < limite:

        yield num*2

        num += 1

devuelvePares = generadorPares(10)

print(next(devuelvePares)) # next
print("Hola")
print(next(devuelvePares))



for numero in devuelvePares:
    print(numero)
```

## next

