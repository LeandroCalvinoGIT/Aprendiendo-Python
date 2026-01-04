""" import unittest

def sumar(a,b):
    return a + b

def dividir(a,b):

    if b == 0:
        raise ValueError("No se puede dividir por 0")
    
    return a // b

class TestCalculadora(unittest.TestCase):

    def test_sumar(self):
        resultado = sumar(10,4)
        self.assertEqual(resultado, 14)

    def test_dividir(self):
        resultado = dividir(10,2)
        self.assertEqual(resultado, 5)

        with self.assertRaises(ValueError):
            dividir(10,0)

if __name__ == '__main__':
    unittest.main() """

import unittest
from tests.saludar import *

class testear(unittest.TestCase):

    def test_saludoCorrecto(self):
        saludo = formar_saludo("Leandro", 21)
        self.assertEqual(saludo,"Hola! mi nombre es Leandro, y tengo 21 años")
    
    def test_dividir(self):
        resultado = dividir(10,2)
        self.assertEqual(resultado, 5)

        with self.assertRaises(ValueError):
            dividir(10,0)

if __name__ == '__main__':
    unittest.main()