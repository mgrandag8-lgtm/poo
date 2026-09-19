class Grados:
    def __init__(self, celsius):
        self.celsius = celsius

    def convertir(self):
        fahrenheit = (self.celsius * 9 / 5) + 32
        return fahrenheit


temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

grados = Grados(temperatura)

print(temperatura, "grados Celsius son", grados.convertir(), "grados Fahrenheit")