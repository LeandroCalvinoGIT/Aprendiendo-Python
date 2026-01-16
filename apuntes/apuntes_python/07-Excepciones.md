# EXCEPCIONES

Errores que ocurren durante la ejecución del programa (EJ: division por 0).

## MANEJO O CONTROL DE EXCEPCION:

Identificar la linea que genera el error y evitar que se ejecute, para permitir que el programa continue.

Al saltar una excepcion se nos informa:
- La pila de llamadas (la linea donde salto el error, y de donde provienepie)
- El tipo de error (Ej: ZeroDivisionError)

Tenemos las palabras reservadas **try** y **except** para atrapar dichos errores

Estructura:

```python
    try:
        # Código que puede fallar
    except ErrorTipo:
        # Qué hacer si falla
    else:
        # Qué hacer SI NO FALLÓ
    finally:
        # Se ejecuta siempre
```

```python
def dividir():
    
    #Intenta ejecutar el codigo
    try:
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo numero: "))
        return num1/num2
    #Si salta el error, ejecuta el código del except
    except ValueError: #excepcion por ingresar algo no numero al int()
        print("Numero ingresados invalidos")
        return "Ingresa un valor correcto"
    except ZeroDivisionError: #excepcion por dividir por 0
        print("no se puede didivir por 0")
        return "Operación Errónea"
    finally:
        print("Cálculo terminado")
```

- Se intenta ejecutar el bloque dentro de try
- En caso de lanzarse una excepcion, se ejecutará el codigo dentro del except correspondiente al tipo de excepcion
- En caso de usar **except** sin un tipo de error, el mismo atrapara cualquier tipo de excepción
  
### FINALLY

Usando **finally** se asegura de que esa porción de código se ejecute siempre.

### RAISE:

Usando **raise** se puede lanzar una excepción personalizada

```python
def evaluaEdad(edad):

    if edad < 0:
        raise ValueError("No se permiten edades Negativas")

    if edad < 18:
        return "Menor de edad"
    else:
        return "Mayor de edad"
```

## TIPOS DE ERRORES:

- SyntaxError:          No se puede atrapar con try/except ya que python directamente no ejecutará
- IdentationError:      Al identar de forma errónea
- ValueError:           Al querer convertir tipos de datos (int("hola"))
- TypeError:            Al mezclar tipos de datos, ej: 5 + "hola" o len(5)
- ZeroDivisionError:    Al dividir por 0
- IndexError:           Al querer acceder a un índice que no existe
- KeyError:             Al querer acceder a una key inexistente de un diccionario
- NameError:            Variable no definida, por error de tipeo o fuera de scope
- AttributeError:       El objeto no tiene ese método/atributo
  