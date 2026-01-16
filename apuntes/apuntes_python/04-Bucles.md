# BUCLES:

## KEYWORDS:
**break**        # sale del bucle
**continue**       # saltea desde ese punto a la siguiente iteración
**pass**           # no hace nada

## WHILE: 

Ejecuta un bloque de código mientras que la condición se cumpla

    while condición:
        instrucción
    
## FOR: 

Ejecuta un bloque de código una cantidad de veces prefijada

    for variable in (iterable):
        instrucción

La función ***range(a,b,c)*** genera una lista de los numeros iniciando en a y terminando en b-1 con salto c
La función **reversed()** da vuelta el orden de una lista

### enumerate(iterable)

La funcion enumarate() convierte un iterable en una pares indice / valor:

Ej:
colores = ["rojo", "verde", "azul"]

for i, color in enumerate(colores, start = n):
    print(i, color)

Salida:

n rojo
n+1 verde
n+2 azul

## BUCLES ANIDADOS: Un bucle adentro de otro

EJ: for x in range(3):                      # imprime:
        for y in range(1,11):               # 1-2-3-4-5-6-7-8-9-10-/
            print(y, end="-")               # 1-2-3-4-5-6-7-8-9-10-/
        print("/")                          # 1-2-3-4-5-6-7-8-9-10-/

