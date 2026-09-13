class Notas:
    def __init__(self):
        self.notas = [7, 8.5, 6, 9, 10, 5.5]

    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def maxima(self):
        return max(self.notas)

    def minima(self):
        return min(self.notas)


notas = Notas()

print(f"Promedio: {notas.promedio():.2f}")
print(f"Nota máxima: {notas.maxima():.2f}")
print(f"Nota mínima: {notas.minima():.2f}")