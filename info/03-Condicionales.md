# CONDICIONAL

Un **condicional** es una estructura de control de flujo que permite tomar una desición en base a una sentencia.

En resumen, es realizar un *statement* y según la veracidad del mismo el programa hará una cosa u otra.

## IF: 

Se usa para ejecutar un bloque de código solo *si* se cumple una condición

Estructura:

if condición:
    instrucción
elif
    instrucción
else
    instrucción

```python
if 5 > 7:
    print("algo")
elif 5 >5:
    print("otro")
else:
    print("otro otro")
```

## EXPRESIÓN CONDICIONAL: 

Otra sintaxis para escribir un condicional en una linea

Estructura:
X if condición else Y

`print("Cumple" if true else "No cumple")`

## MATCH CASE (SWITCH)

Es una alternativa para if anidado, similar al switch de c, pero no comparte ventajas y es solo sugar syntax

Estructura:

```python
match variable:
    case caso1:
        accion1
    case caso2:
        accion2
    case _:
        default #Entra en este caso si ningun otro funciona.
```