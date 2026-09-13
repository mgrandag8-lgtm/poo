class Grados:
    def __init__(self, celsius):
        self.celsius = celsius

    def celsius_to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

grados_C = float(input("ingrese la temperatura en grados celsius:"))
grados = Grados(grados_C)
print(f"{grados_C} grados celsius son {grados.celsius_to_fahrenheit()} grados fahrenheit")

        