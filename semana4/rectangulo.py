class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area_rectangulo(self):
        return self.base * self.altura


base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

rectangulo = Rectangulo(base, altura)

print("El área del rectángulo es:", rectangulo.area_rectangulo())