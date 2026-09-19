cantidad = int(input("Ingrese cuántos números desea usar: "))

pares = 0
impares = 0

for contador in range(cantidad):
    valor = int(input("Escriba un número: "))

    if valor % 2 == 0:
        pares = pares + valor
    else:
        impares = impares + valor

print("Total de números pares:", pares)
print("Total de números impares:", impares)