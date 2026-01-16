LISTAS COMPRIMIDAS: [expression for value in iterable if condition]
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