# FUNCIONES: 

- Bloque de código agrupado y reutilizable, que se encarga de una tarea específica. 
- Pueden devolver valores, y tener o no parámetros/argumentos
- También se las denomima métodos cuando pertenecen a una clase/objeto

## SINTAXIS:

```python
def nombre_funcion(argumento1, argumetno2 = "valor x defecto"):
    # instrucciones
    return(valor) # opcional
```

## INVOCACION:
nombre_funcion(argumentos)

## Return: 
termina una función y devuelve algun parametro

## TIPOS DE PARAMETROS:

1. POSICIONAL:  Los argumentos se asignan de acuerdo a su posicion
2. DEFAULT:     Los parametros tienen un valor x defecto que se pisa si se recibe un argumento, van despúes que los posicionales
3. KEYWORD:     Los argumentos se pasan de la manera keyword = valor, se colocan siempre después que los posicionales
4. ARBITRARIOS: No hay un número predefinido de argumentos, se subdivide:
   1.     *args:  Se pasa cómo argumento una tupla conteniendo argumentos posicionales
   2.      **kwargs:  Se pasa cómo argumento un diccionario conteniendo los argumentos keywords