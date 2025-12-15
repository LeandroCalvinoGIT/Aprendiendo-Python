FUNCIONES: Bloque de código reutilizable

DEFINICION:
    def funcion(argumento1, argumetno2 = valor x defecto):
        instrucciones

INVOCACION:
    funcion()

Return: termina una función y devuelve algun parametro

TIPOS DE PARAMETROS:

    1) POSICIONAL:  Los argumentos se asignan de acuerdo a su posicion
    2) DEFAULT:     Los parametros tienen un valor x defecto que se pisa si se recibe un argumento, van despúes que los posicionales
    3) KEYWORD:     Los argumentos se pasan de la manera keyword = valor, se colocan siempre después que los posicionales
    4) ARBITRARIOS: No hay un número predefinido de argumentos, se subdivide:

        4.1)    *args:  Se pasa cómo argumento una tupla conteniendo argumentos posicionales
        4.2) **kwargs:  Se pasa cómo argumento un diccionario conteniendo los argumentos keywords


