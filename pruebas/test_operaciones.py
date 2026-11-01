import unittest

from calculadora.controlador import Controlador
from calculadora.operaciones import OperacionesAdicionales


class PruebasOperacionesAdicionales(unittest.TestCase):
    def setUp(self):
        self.operaciones = OperacionesAdicionales()

    def test_restar(self):
        self.assertEqual(self.operaciones.restar(8, 3), 5)

    def test_dividir(self):
        self.assertEqual(self.operaciones.dividir(9, 3), 3)

    def test_controlador_formatea_resultados(self):
        controlador = Controlador()
        self.assertEqual(controlador.operar("restar", "8", "3"), "5")
        self.assertEqual(controlador.operar("dividir", "7", "2"), "3.5")

    def test_controlador_rechaza_division_por_cero(self):
        controlador = Controlador()
        self.assertEqual(
            controlador.operar("dividir", "8", "0"),
            "No se puede dividir por cero",
        )


if __name__ == "__main__":
    unittest.main()
