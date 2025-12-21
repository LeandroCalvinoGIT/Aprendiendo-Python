# OBJETOS

# CLASES:

## Sintaxis:

```python

# Definir una clase
class NombreDeClase():
    # Atributos
    atributo1 = "string"
    atributo2 = 0
    atributo3 = True
        
    # Método constructor de la clase
    def __init__(self, atributo1, atributo2, atributo3):
        self.atributo1 = atributo1
        self.atributo2 = atributo2
        self.atributo3 = atributo3

# Instanciar una clase con valores:
instancia1 = NombreDeClase("atributo1", 30, False)

# Modificar atributos
instancia1.atributo2 = 21

# Consultar atributos
print("El atrtibuto2 de instancia1 es:".instancia1.atributo2)

```

- Funcion vs Método: Un metodo es una funcion que pertenece a una clase, las funciones no pertenecen a ninguna clase

## ENCAPSULAMIENTO:

### ENCAPSULAR VARIABLES Y MÉTODOS:

Se logra precediendo el nombre de una con __ para que solo sea accesible desde dentro de la misma clase.

# HERENCIA

Para heredar de una clase, se debe definir la misma de la siguiente manera:

```python
class ClasePadre():
    def __init__(self, atributoPadre):
        self.atributoPadre = atributoPadre

class ClaseHija(ClasePadre):
    def __init__(self, atributoPadre, atributoHijo):
        super().__init__(atributoPadre)
        self.atributoHijo = atributoHijo
```

Para redefinir comportamiento, simplemente se sobreescribe el método:

```python
class ClasePadre():
    def __init__(self, atributoPadre):
        self.atributoPadre = atributoPadre

    def metodo(self):
        return 5

class ClaseHija(ClasePadre):
    def __init__(self, atributoPadre, atributoHijo):
        super().__init__(atributoPadre)
        self.atributoHijo = atributoHijo

    def metodo(self):
        return 15
```

## VERIFICAR TIPO DE CLASE:

Se puede usar la función `isinstance(objeto, clase)` para verificar si un objeto es instancia de una cierta clase

ejemplo:
```python
class Clase():
    pass

objeto = Clase()

print(isinstance(objeto, Clase)) #Imprime True
```