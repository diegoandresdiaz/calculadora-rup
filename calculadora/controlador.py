from calculadora.modelo import Calculadora
class Controlador:
      def __init__(self):
                self.modelo = Calculadora()
                self.operaciones = {
                    "sumar": self.modelo.sumar,
                    "multiplicar": self.modelo.multiplicar,
                }

      def operar(self, operacion, texto1, texto2):
                try:
                              a = float(texto1)
                              b = float(texto2)
except ValueError:
            return "Ingrese números válidos"

        resultado = self.operaciones[operacion](a, b)
        if resultado.is_integer():
                      resultado = int(resultado)
                  return str(resultado)
