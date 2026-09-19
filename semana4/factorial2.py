class Calculo:
    def __init__(self, n, r):
        self.n = n
        self.r = r

    def factorial(self, valor):
        total = 1

        for numero in range(1, valor + 1):
            total *= numero

        return total

    def calcular(self):
        arriba = self.factorial(self.n)
        abajo = self.factorial(self.r) * self.factorial(self.n - self.r)

        return arriba / abajo


n = int(input("Ingrese el valor de n: "))
r = int(input("Ingrese el valor de r: "))

operacion = Calculo(n, r)

print("Resultado de la combinatoria:", operacion.calcular())