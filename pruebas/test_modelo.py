import unittest
from calculadora.modelo import Calculadora


class PruebasCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_sumar(self):
        self.assertEqual(self.calc.sumar(5, 3), 8)

    def test_sumar_negativos(self):
        self.assertEqual(self.calc.sumar(-2, 0.5), -1.5)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(1000, 34), 34000)

    def test_multiplicar_por_cero(self):
        self.assertEqual(self.calc.multiplicar(7, 0), 0)


if __name__ == "__main__":
    unittest.main()
