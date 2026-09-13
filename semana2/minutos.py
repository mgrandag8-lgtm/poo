minutos = int(input("Ingrese la cantidad de minutos: "))

horas = minutos // 60
minutos_restantes = minutos % 60

print(f"{horas} horas {minutos_restantes} minutos")