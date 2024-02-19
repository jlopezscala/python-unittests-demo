import unittest
from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_sumar(self):
        self.assertEqual(self.calc.sumar(10, 5), 15)

    def test_restar(self):
        self.assertEqual(self.calc.restar(10, 5), 5)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 7), 21)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)