class Anio:
    def __init__(self, valor):
        self.valor = valor

    def comprobar(self):
        if self.valor % 4 == 0 and self.valor % 100 != 0:
            return True
        elif self.valor % 400 == 0:
            return True
        else:
            return False


numero_anio = int(input("Escriba un año: "))

resultado = Anio(numero_anio)

if resultado.comprobar():
    print(numero_anio, "es un año bisiesto")
else:
    print(numero_anio, "no es un año bisiesto")