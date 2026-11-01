from calculadora.modelo import Calculadora
from calculadora.operaciones import OperacionesAdicionales


class Controlador:
    def __init__(self):
        self.modelo = Calculadora()
        self.operaciones_adicionales = OperacionesAdicionales()
        self.operaciones = {
            "sumar": self.modelo.sumar,
            "multiplicar": self.modelo.multiplicar,
            "restar": self.operaciones_adicionales.restar,
            "dividir": self.operaciones_adicionales.dividir,
        }

    def operar(self, operacion, texto1, texto2):
        try:
            a = float(texto1)
            b = float(texto2)
        except ValueError:
            return "Ingrese números válidos"

        try:
            resultado = self.operaciones[operacion](a, b)
        except ZeroDivisionError:
            return "No se puede dividir por cero"

        if resultado.is_integer():
            resultado = int(resultado)
        return str(resultado)
