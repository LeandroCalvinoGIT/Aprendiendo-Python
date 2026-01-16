# INPUT

La función **input()** solicita al usuario que ingrese datos y los devuelve en forma de string

Ej:

```python
nombre = input("Porfavor, ingrese su nombre)
print(f"Su nombre es: {nombre})
```

En el caso de querer recibir la información cómo dato numérico para poder operar con ella, es necesario realizar la conversión explícita del dato, de la siguiente forma:

```python
edad = int(input("ingrese su edad: "))
edad += 1
print(f"el próximo año tendrá {edad} años")
```

# OPERADORES

## ASIGNACIÓN:

El operador **=** Sirve para asignar un valor a una variable

```python
numero = 12
```

## ARITMETICA:

Los siguientes símbolos representan las siguientes operaciones:

= Asignar                  
\+ Suma                      += Incrementar  
\- Resta                     -= Decrementar
\* Multiplicación            *= Multiplicar
/ División                  /= Dividir
// División entera          
% Módulo (resto)
** Potenciación             **= Exponente

Ej:

```python
numero = 12
numero += 8
print(numero) #Mostrara en consola un 20
```

### REDONDEO: 

La función round(valor, decimales) redondea un valor al entero(int) más cercano

Ej:
```python
    num1 = 3.14
    num2 = 3.68
    print(round(num1))  # va a devolver el entero 3
    print(round(num2))  # va a devolver el entero 4
    round(num1,1)       #va a devolver el número 3.1
```
   
### VALOR ABSOLUTO: 

La función abs() devuelve el valor absoluto de un númer

```python
    num = -23
    print(abs(num)) # va a devolver 23
```
    

### POTENCIA: 
La función pow(base, exp) eleva la base al exponenete indicado y devuelve el resultado

`print(pow(2,5)) # va a devolver 32`

### MÁXIMO: 
La función max() devuelve el máximo de sus parámetros

### MÍNIMO: 
La función min() devuelve el mínimo de sus parámetros

### MÓDULO DE MÁTEMATICA: import math

math.pi --> valor de el número pi
math.e --> valor de el número e

math.sqrt()  --> raíz cuadrada de un número

math.ceil()  --> Redondea un número float para arriba
math.floor() --> Redondea un número float para abajo

## COMPARACIÓN

 Los siguientes símbolos representan las siguientes operaciones:

==  Igual
!=  Distinto
\>   Mayor que
<   Menor que
\>=  Mayor o igual
<=  Menor o igual

Los resultados de comparar son siempre booleanos true o false

## LÓGICOS

Las siguientes keywords y símbolos sirven como operadores lógicos

&&  and
||  or
!   not

## BINARIOS

&   and binario
|   or binario
^   xor binario
\-   complemento (invierte bits)
<<  left shift binario
\>>  right shift binario
