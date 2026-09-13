class Anio:
    def __init__(self, anio):
        self.anio = anio

    def es_bisiesto(self):
        if self.anio % 400 == 0:
            return True
        elif self.anio % 100 == 0:
            return False
        elif self.anio % 4 == 0:
            return True
        else:
            return False


anio = int(input("Ingrese un año: "))

dato = Anio(anio)

if dato.es_bisiesto():
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")