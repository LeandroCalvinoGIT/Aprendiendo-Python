CONDICIONALES:

IF: Se usa para ejecutar un bloque de código solo si se cumple una condición

Estructura:

if condición:
    instrucción
elif
    instrucción
else
    instrucción

OPERADORES LÓGICOS: OR (|), AND, NOT

EXPRESIÓN CONDICIONAL: X if condición else Y
EJ: print("Cumple" if true else "No cumple")

MATCH CASE: Alternativa a usar muchos elifs, mas comprensible.

Se usa el case _ para el "Default"

EJ: 

dia = "Lunes"

match dia:
    case "Lunes":
        print("Es lunes")
    case "martes:
        print("Es martes")
    case _:
        print("nose xd")

funcion:

def is_weekend(dia):
    match dia:
        case "Sabado" | "Domingo":
            return True
        case _:
            return False
