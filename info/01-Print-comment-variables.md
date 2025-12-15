# Comentarios:

## En Linea

Se comenta una linea iniciando la misma con **numeral #**

#esto es un comentario en linea

## En bloque

Se comenta en bloque usando las **comillas tripes """ """**

""" triple comilla 
para comentario 
en bloques"""

---

# Imprimir en pantalla: 
```python
    print("Hola Mundo!")
```
Agregando un segundo parámetro end="" se modifica el caracter final (por defecto es newline)


```python
   print("HOLA", end="x")  # imprime HOLAx
```

---

# Variables:

Se definen como nombre = valor

Ej:

```python
    edad = 21
    print(edad) # Esto muestra en consola el 21
```

Las variables se escriben usando la convención de **snake_case**
Se usa el operador **=** para asignar un valor a dicha variable

```python
    primer_variable = valor
```

Las variables son *mutables*, por lo que se puede **modificar su valor**

```python
    variable = 5
    print(variable) # Esto muestra en consola el 5
    variable = 10
    print(variable) # Esto muestra en consola el 10
```

---

# Tipos de Datos

Los tipos de datos básicos son los siguientes:
    Entero (int)            ej: 305
    Flotante (float)        ej: 203.43
    Cadena de texto(str)    ej: "Hola mundo!"   
    Booleano (bool)         ej: True False
    Nulo (NoneType)         ej: None


La función **type()** devuelve el tipo de dato que contiene una variable cualquiera
La funcion **isinstance(variable,tipo)** devuelve un booleano si hay match

Ej: 

```python
    variable = 5
    print(type(variable)) # Es de tipo int
    print(isinstance(variable,str)) # Imprime false
```

## Typecasting

Para pasar de un tipo de dato a otro se utilizan las funciones: int() , str() , bool(),  float()

Ej: edad = 20
    edad = float(edad)
    print(type(edad))   #esto va a devolver float

No todo se puede castear (convertir letras a numero por ejemplo)

## Variable vacía

Se crea usando el typecast sin asignar valor

Para strings:

```python
    variable_str_vacia = ""
    variable_str_vacia = str()
```

Por ej, Para strings:

```python
    variable_str_vacia = ""
    variable_str_vacia = str()
```

## Concatenar variables

Se usa el siguiente formato:

```python
nombre = "Leandro"
edad = 21
texto = f"Mi nombre es {nombre} y tengo {str(edad)} años"
print(texto)
```
