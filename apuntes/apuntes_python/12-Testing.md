# TESTING

Un test sirve para verificar que el código se comporte como se esperaba

## assert

Verifica que una función se comporte como se esperaba:

```python
def sumar(a,b):
    return a + b

assert sumar(2,2) == 4

def es_par(n):
    return n % 2 == 0

assert es_par(4) is True
assert es_par(7) is False
```

## test de errores

Podemos usar try y except para testear excepciones que creamos:

```python
def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

try:
    dividir(10, 0)
    assert False
except ValueError:
    assert True
```

# UNIT TESTING

Se utiliza el builtin modulo **unittesting**. Crear un nuevo archivo test_nombre.py o nombre_test.py

El **unit test** chequea que una aspecto en específico de una función es correcto
El **unit case** es un conjunto de **unit tests**, chequea que una función entera funciona bien

# ASSERT METHOD:

El modulo trae incluido varios metodos assert:

- assertEquals(a,b)             -> a == b
- assertNotEquals(a,b)          -> a != b
- assertTrue(x)                 -> bool(x) is True
- assertFalse(x)                -> bool(x) is False

- assertIn(item, coleccion)     -> el item esta en la coleccion
- assertNotIn(item, coleccion)  -> el item no está en la coleccion

- assertIsInstance(objeto,Clase)                   -> el objeto es una instancia de esa clase

- assertRaises(excepction, function, arguments) -> La funcion levanta el error
  
## Estructura:

Una vez importado el modulo de testing, se crea una clase que herede de **unittest.TestCase**
A dicha clase, se le define cada test como un método *test_nombre(self)* (si o si empezar con test_)

Ejemplo:
```python
import unittest

class test_funcion(unittest.TestCase):
    def test_funcionalidad(self):
        self.assertEqual(funcion(a,b),resultado_esperado)

    def test_levantaError(self):
        with self.assertRaises(tipoError):
            funcion(a,c)
```

## Ejecución:

Para hacer que los test se ejecuten desde el archivo de tests (ya que por defecto se deberían ejecutar
desde el módulo), debemos usar el siguiente código:

```python
if __name__ == '__main__':
    unittest.main()
```
## setUp tearDown

Se pueden usar ambos metodos para crear y destruir elementos solo usados en los tests:

```python
# Se ejecutra antes de cada test
def setUp(self):
    self.objeto = Objeto(args)

# Se ejecuta al final de cada test
def tearDown(self):
    pass
```