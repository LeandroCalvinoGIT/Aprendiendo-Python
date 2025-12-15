ITERABLES: Objetos/colecciones que pueden devolver sus elementos uno a la vez, pudiendo ser iterados en un loop

Son iterables: -Listas
               -Tuplas
               -Sets
               -Diccionarios
               -Strings

EJ:
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

