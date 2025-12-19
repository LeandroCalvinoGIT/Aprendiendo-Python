# COLECCIONES: 
Variables que almacenan varios valores

List  = []   ordenada y modificable, puede haber duplicados
Tuple = ()   ordenada e inmodificable, puede haber duplicados, más rápida.
Set   = {}   desordenada e inmutable, no duplicados, se puede añadir/quitar

len(coleccion)              # devuelve la cant de elementos

## IN: 
Devuelve un booleano que indica si el elemento está en la colección

    ej:elemento1 in lista      # devuelve True

----------------------------------------------------------------------------------------------------------

## LISTAS: 
lista = [elemento1, elemento2, elemento3]
len(lista)              # devuelve la cant de elementos

print(lista[n])         # imprime el elemento en la posicion n
print(lista[:])         # imprime todos los elementos
print(lista[-1])        # imprime el ultimo elemento (inidice negativo cuenta desde atras)

print(lista[:3])       # accede a los tres primero elementos
print(lista[a:b])       # accede a los elementos desde a (incluido) hasta b (sin incluir)
print(lista[:b])        # Si se omite el primer indice, se asume que es desde el 0 hasta b
print(lista[a:])        # Si se omite el segundo indice, se asume que es desde el a hasta el último


### MÉTODOS EN LISTAS:

El método .append(elemento) **añade** un elemento al final de la lista
El método .extend(lista) **añade los elementos de otra lista** al final de la lista (concatena)
    también se puede hacer concatenando: lista1 + lista2
    usando el * se repite la lista
El método .remove(elemento) **elimina** un elemento de la lista
El método .pop() **elimina el último** elemento de la lista
El método .insert(index, element) **inserta** un elemento en la posición indicada
El método .sort() **ordena** la lista en orden alfabético
El método .reverse() **Invierte** el orden de la lista
El método .clear() **elimina todos** los elementos de la lista
El método .index(elemento) **devuelve el index** de la primer aparicion del elemento, da error si no esta
El método .count(elemento) **devuelve la cant de veces** que dicho elemento de encuentra en la lista

----------------------------------------------------------------------------------------------------------

## SET:
Son colecciones desordenadas y mutables de objetos sin repeticion
set = {elemento1, elemento3, elemento4, elemento2}

print(set)  # imprime sin un orden determinado
la funcion set(coleccion) genera un set con los elementos de la coleccion

### MÉTODOS DE SET:

El método .add(elemento) añade un elemento al conjunto
El método .remove(elemento) elimina un el elemento del conjunto
El método .pop() elimina un elemento al azar
El método .clear() elimina todos los elementos

----------------------------------------------------------------------------------------------------------

## TUPLAS:
tuple = (elemento1, elemento2, elemento3)

- Son listas **inmutables**
- No se pueden añadir ni eliminar elementos
- Si permiten extraer porciones como una nueva tupla
- Si permiten comproban que un elemento pertenece.

### Ventajas:

- Más rápidas
- Menos espacio (mayor optimización)
- Formatean Strings
- Pueden utilizarse como KEYS en diccionarios

### MÉTODOS DE TUPLA:

El método .index(elemento) devuelve la posición de un elemento
El método .count(elemento) devuelve la cantidad de el elemento en la tupla

### DESEMPAQUETAR TUPLA

"Descomoponer" los valores de la tupla Asignandolos a variables independientes
tupla = ("Lean", 6, 12, 2004)
nombre, dia, mes, anio = tupla

----------------------------------------------------------------------------------------------------------

## TYPECAST: 
lista = **list(tupla)**     # Construye una lista a partir de la tupla
tupla = **tuple(lista)**    # Construye una tupla a partir de la lista

## COLECCIONES 2D:

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

----------------------------------------------------------------------------------------------------------
## DICCIONARIOS: 
Colección de pares {key:value} ordenados y modificables, no repetidos

ej:     Capitals = {"Argentina":"CABA,
                    "USA":"Washington D.C.",
                    "Peru":"Lima"}

MÉTODOS DE DICCIONARIOS:

El método .get(key) devuelve el value asociado
El método .update({key:value}) agrega un elemento al diccionario
    también `diccionario[key] = value` agrega el elemento O modifica el valor de la clave asociada
El método .pop(key) elimina el par asociado
    también `del diccionario[key]`
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

