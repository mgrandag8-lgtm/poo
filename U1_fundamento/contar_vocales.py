class Frase:
    def __init__(self, texto):
        self.texto = texto

    def contar_vocales(self):
        contador = 0

        for letra in self.texto.lower():
            if letra in "aeiou":
                contador += 1

        return contador


texto = input("Ingrese una frase: ")

frase = Frase(texto)

print("Cantidad de vocales:", frase.contar_vocales())