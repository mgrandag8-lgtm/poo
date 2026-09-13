class Lista:
    def __init__(self):
        self.datos = ["a", "b", "a", "c", "b", "d"]

    def sin_duplicados(self):
        vistos = set()
        nueva_lista = []

        for elemento in self.datos:
            if elemento not in vistos:
                vistos.add(elemento)
                nueva_lista.append(elemento)

        return nueva_lista


lista = Lista()

print(lista.sin_duplicados())