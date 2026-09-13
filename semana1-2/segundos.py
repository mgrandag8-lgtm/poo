segundos = int(input("Ingrese la cantidad de segundos: "))

horas = segundos // 3600

resto = segundos % 3600

minutos = resto // 60

segundos_finales = resto % 60

print(f"{horas} horas, {minutos} minutos y {segundos_finales} segundos")