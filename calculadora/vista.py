import tkinter as tk
from calculadora.controlador import Controlador

AZUL = "#1565c0"
BLANCO = "#ffffff"
class Vista:
    def __init__(self):
        self.controlador = Controlador()
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")
        self.ventana.config(bg=BLANCO, padx=30, pady=20)

        self.salida = tk.StringVar()

        tk.Label(self.ventana, text="dato 1", bg=BLANCO, fg=AZUL).grid(row=0, column=0, pady=5)
        self.dato1 = tk.Entry(self.ventana)
        self.dato1.grid(row=0, column=1, columnspan=2)

        tk.Label(self.ventana, text="dato 2", bg=BLANCO, fg=AZUL).grid(row=1, column=0, pady=5)
        self.dato2 = tk.Entry(self.ventana)
        self.dato2.grid(row=1, column=1, columnspan=2)

        tk.Button(self.ventana, text="sumar", bg=AZUL, fg=BLANCO,
                  command=lambda: self.calcular("sumar")).grid(row=2, column=1, pady=10)
        tk.Button(self.ventana, text="multiplicar", bg=AZUL, fg=BLANCO,
                  command=lambda: self.calcular("multiplicar")).grid(row=2, column=2)

        tk.Button(self.ventana, text="restar", bg=AZUL, fg=BLANCO,
                  command=lambda: self.calcular("restar")).grid(row=3, column=1, pady=10)
        tk.Button(self.ventana, text="dividir", bg=AZUL, fg=BLANCO,
                  command=lambda: self.calcular("dividir")).grid(row=3, column=2)

        tk.Label(self.ventana, text="resultado", bg=BLANCO, fg=AZUL).grid(row=4, column=0, pady=5)
        tk.Entry(self.ventana, textvariable=self.salida, state="readonly").grid(row=4, column=1, columnspan=2)

    def calcular(self, operacion):
        resultado = self.controlador.operar(operacion, self.dato1.get(), self.dato2.get())
        self.salida.set(resultado)

    def iniciar(self):
        self.ventana.mainloop()
