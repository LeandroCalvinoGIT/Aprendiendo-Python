#01: Pide el nombre del usuario y muestra un saludo personalizado.

""" nombre = input("Ingresa tu nombre:")
print(f"Hola {nombre}, Bienvenid@ a python!") """

#02: Pide dos números al usuario y muestra la suma.

""" num1 = float(input("Porfavor ingresa el primer número: "))
num2 = float(input("Porfavor ingresa el segundo número: "))
print(f"La suma es: {num1 + num2}") """

#03: Pide dos números y muestra las operaciones básicas

""" num1 = float(input("Porfavor ingresa el primer número: "))
num2 = float(input("Porfavor ingresa el segundo número: "))

#Suma
print(f"La suma es: {num1 + num2}")
#Resta
print(f"La resta es: {num1 - num2}")
#Producto
print(f"El producto es: {num1 * num2}")
#División
print(f"La división es: {num1 / num2}") """

#04: Pide la edad actual y muestra qué edad tendrá dentro de 10 años.

""" edad = int(input("Porfavor ingresa tu edad: "))
print(f"En 10 años tendrás {edad + 10} años :D") """

#05: Área de un rectángulo: Pide base y altura y calcula el área.

""" base = float(input("Porfavor ingresa la medida de la base: "))
altura = float(input("Porfavor ingresa la medida de la altura: "))
area = base * altura
print(f"El área del rectángulo es: {area}") """

#06: Promedio de tres notas: Pide tres notas y calcula el promedio.

""" nota1 = int(input("Ingresa la primer nota: "))
nota2 = int(input("Ingresa la segunda nota: "))
nota3 = int(input("Ingresa la tercer nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"El promedio del alumn@ es {promedio}") """

#07: Conversión de tipos: Pide un número entero y muestra como int, float, str

""" numero = input("Ingresa un numero:")
num_float = float(numero)
num_int = int(num_float)

print(f"El numero ingresado en formato {type(numero)} es {numero}")
print(f"El numero ingresado en formato {type(num_int)} es {num_int}")
print(f"El numero ingresado en formato {type(num_float)} es {num_float}") """

#08: Precio final con IVA: Pide el precio de un producto y calcula el precio final con IVA del 21%

""" precio = float(input("Ingresa el precio del producto sin impuestos: "))

precio_final = precio + precio * 0.21

print(f"El precio total con el IVA será de: {precio_final}")"""

#09: comparación: Pide dos números y muestra el resultado

""" num1 = float(input("Porfavor ingresa el primer número: "))
num2 = float(input("Porfavor ingresa el segundo número: "))

print(f"Los números son Iguales? {num1 == num2}")
print(f"El primero es mayor? {num1 > num2}")
print(f"El segundo es mayot? {num1 < num2}") """

#10: COMPRAS! 

# ============================================
# EJERCICIO FINAL INTEGRADOR
# Simulador simple de compra
# ============================================
#
# Consigna:
# Crear un programa que simule una compra en un comercio.
#
# El programa debe:
# 1. Pedir el nombre del producto
# 2. Pedir el precio unitario del producto
# 3. Pedir la cantidad de unidades
# 4. Calcular:
#    - Subtotal (precio * cantidad)
#    - IVA (21% del subtotal)
#    - Total a pagar (subtotal + IVA)
# 5. Mostrar un resumen completo de la compra
#
# Fórmulas:
# subtotal = precio * cantidad
# iva = subtotal * 0.21
# total = subtotal + iva
#
# Reglas:
# - Usar comentarios
# - Usar print() para mostrar resultados
# - Usar input() para pedir datos al usuario
# - Usar typecast (float e int)
# - Usar operadores aritméticos
# - Usar f-strings
# - NO usar if, while, funciones, listas ni try/except
#
# Ejemplo de entrada:
# Ingrese el nombre del producto: Auriculares
# Ingrese el precio unitario: 12500.50
# Ingrese la cantidad: 2
#
# Ejemplo de salida (formato aproximado):
# ----- RESUMEN DE COMPRA -----
# Producto: Auriculares
# Precio unitario: $12500.5
# Cantidad: 2
# Subtotal: $25001.0
# IVA (21%): $5250.21
# Total a pagar: $30251.21
# ----------------------------
#
# Desafíos opcionales:
# - Mostrar el tipo de dato de precio, cantidad y total
# - Calcular el precio final por unidad con IVA
# - Mostrar los valores con 2 decimales usando round()
#
# ============================================

# Input de datos:

nombre = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad = int(input("Ingrese la cantidad de unidades: "))

# Operaciones

iva_unitario = precio_unitario * 0.21
subtotal = precio_unitario * cantidad
iva = iva_unitario * cantidad
precio_total = subtotal + iva

# Output de resultados

print("----- RESUMEN DE COMPRA -----")
print(f"Producto: {nombre}, {type(nombre)}")
print(f"Precio Unitario: {precio_unitario}, {type(precio_unitario)}")
print(f"Cantidad: {cantidad}", {type(cantidad)})
print(f"Subtotal: {subtotal}")
print(f"Iva por unidad: {round(iva_unitario,2)}")
print(f"IVA total (21%): {round(iva,2)}")
print(f"Total a pagar: {round(precio_total,2)}")
print(" ----------------------------")