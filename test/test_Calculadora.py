import unittest

from src.Calculadora import suma, resta, multiplicacion

class CalculadoraTest(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(3, 2), 5)
        
    def test_resta(self):
        self.assertEqual(resta(5, 2), 3)
        
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(3, 2), 6)