# ==================================================
# EJERCICIO 1 - NORMALIZAR TEXTO
# ==================================================
# Pedir al usuario que ingrese un texto
# El programa debe:
# - Mostrar la cantidad total de caracteres (len)
# - Mostrar el texto:
#   * en mayúsculas
#   * en minúsculas
#   * con la primera letra en mayúscula
#
# Ejemplo input:
#   "   hOLa MuNdO   "
#
# Tip:
# - Usar strip() antes de procesar el texto

""" texto = input("Ingresa un texto: ")
texto = texto.strip()

print("-------------------------")
print(f"Cantidad de caracteres: {len(texto)}")
print("Mayúscula:")
print(texto.upper())
print("Minúscula:")
print(texto.lower())
print("Capitalizado:")
print(texto.capitalize())
print("-------------------------") """

# ==================================================
# EJERCICIO 2 - BUSQUEDA DE CARACTERES
# ==================================================
# Pedir al usuario una palabra
# Pedir luego un carácter a buscar
#
# El programa debe:
# - Mostrar la primera posición del carácter (find)
# - Mostrar la última posición del carácter (rfind)
# - Si el carácter no aparece, mostrar un mensaje adecuado
#
# Ejemplo:
#   palabra = "programacion"
#   caracter = "o"

""" palabra = input("Ingresa una palabra: ").lower()
caracter = input("Ingresa un caracter a buscar: ").lower()

primera_aparicion = palabra.find(caracter)
ultima_aparicion = palabra.rfind(caracter)

if primera_aparicion != -1:
    print(f"La primera aparición del caractér {caracter} en la palabra {palabra} es en la posición: {primera_aparicion}")
    print(f"La última aparición del caractér {caracter}  en la palabra {palabra} es en la posición {ultima_aparicion}")
else:
    print(f"El caractér {caracter} no se encuentra en la palabra {palabra}") """

# ==================================================
# EJERCICIO 3 - VALIDACION DE STRING
# ==================================================
# Pedir al usuario que ingrese un código
#
# El programa debe indicar:
# - Si el código es solo numérico (isdigit)
# - Si es solo alfabético (isalpha)
# - Si es alfanumérico (isalnum)
#
# Mostrar exactamente UNA categoría válida
#
# Ejemplo:
#   "ABC123" -> alfanumérico
#   "1234"   -> numérico
#   "abcd"   -> alfabético

""" codigo = input("Ingresa un codigo: ").strip()

if codigo.isdigit():
    print(f"{codigo} --> numérico")
elif codigo.isalpha():
    print(f"{codigo} --> alfabético")
elif codigo.isalnum():
    print(f"{codigo} --> alfanumérico")
else:
    print(f"{codigo} no está en un formato válido") """

# ==================================================
# EJERCICIO 4 - CONTADOR DE PALABRAS
# ==================================================
# Pedir al usuario que ingrese una frase
#
# El programa debe:
# - Eliminar espacios innecesarios (strip)
# - Separar la frase en palabras (split)
# - Mostrar:
#   * La cantidad total de palabras
#   * La palabra más larga (no usar max todavía, hacerlo con bucle)
#
# Ejemplo:
#   " Python es muy poderoso "

def buscar_palabra_mas_larga(palabras):
    longest = palabras[0]

    for palabra in palabras:
        if len(palabra) > len(longest):
            longest = palabra
    
    return longest


""" frase = input("Ingresa una frase: ").strip()

palabras = frase.split()

print("---------------------------------")
print(f"Cantidad de palabras en la frase: {len(palabras)}")
print(f"Palabra mas larga: {buscar_palabra_mas_larga(palabras)}")
print("---------------------------------") """

# ==================================================
# EJERCICIO 5 - LIMPIEZA Y REEMPLAZO
# ==================================================
# Pedir al usuario que ingrese un texto con guiones
#
# El programa debe:
# - Eliminar los guiones de los extremos (strip("-"))
# - Reemplazar todos los guiones internos por espacios (replace)
# - Mostrar el texto final limpio
#
# Ejemplo:
#   "---hola-mundo-python---"
# Resultado:
#   "hola mundo python"

texto_guionado = input("Ingresa un texto con guiones: ").strip("-")

texto_limpio = texto_guionado.replace("-", " ")

print(texto_limpio)

