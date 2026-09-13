class Combinatoria:
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def factorial(self, numero):
        resultado = 1

        for i in range(1, numero + 1):
            resultado = resultado * i

        return resultado

    def combinatoria(self):
        return self.factorial(self.n) / (
            self.factorial(self.k) * self.factorial(self.n - self.k)
        )


n = int(input("Ingrese n: "))
k = int(input("Ingrese k: "))

dato = Combinatoria(n, k)

print("La combinatoria es:", dato.combinatoria())