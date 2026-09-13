class Texto:
    def __init__(self, texto):
        self.texto = texto

    def frecuencia_palabras(self):
        palabras = self.texto.lower().split()
        frecuencia = {}

        for palabra in palabras:
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                frecuencia[palabra] = 1

        return frecuencia

    def palabra_mas_repetida(self):
        frecuencia = self.frecuencia_palabras()
        return max(frecuencia, key=frecuencia.get)


texto = input("Ingrese un texto: ")

dato = Texto(texto)

print("Frecuencia:", dato.frecuencia_palabras())
print("Palabra más repetida:", dato.palabra_mas_repetida())