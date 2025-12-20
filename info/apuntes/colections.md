
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
