class Figura:
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def calcular_area(self):
        area = self.b * self.h
        return area


base = float(input("Escriba la base del rectángulo: "))
altura = float(input("Escriba la altura del rectángulo: "))

dato = Figura(base, altura)

print("Área del rectángulo:", dato.calcular_area())