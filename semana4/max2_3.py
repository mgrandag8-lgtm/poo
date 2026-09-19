class Numeros:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def maximo(self):
        if self.a >= self.b and self.a >= self.c:
            return self.a
        elif self.b >= self.a and self.b >= self.c:
            return self.b
        else:
            return self.c


a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

numeros = Numeros(a, b, c)

print("El número mayor es:", numeros.maximo())