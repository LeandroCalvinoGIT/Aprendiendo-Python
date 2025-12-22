#Se definen como nombre = valor:

edad = 21

print(edad)

# Son mutables, pueden cambiar de valor

variable = 5
print(type(variable)) # Es de tipo int
print(isinstance(variable,str)) # Imprime false


# por defecto
texto = "Hola mundo desde python"
palabras = texto.split() 
print(palabras) # ["Hola", "mundo", "desde", "python"]

# con separador
datos = "10,20,30,40"
datos = datos.split(",")
print(datos)# ["10", "20", "30", "40"]

# con máximo:
palabras2 = texto.split(" ", 2) 
print(palabras2) # ["Hola", "mundo", "desde python"]