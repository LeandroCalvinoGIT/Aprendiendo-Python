def formar_saludo(nombre, edad):
    saludo = f"Hola! mi nombre es {nombre}, y tengo {edad} años"
    return saludo

def dividir(a,b):
    if b == 0:
        raise ValueError("No se puede dividir por 0")
    
    return a // b