N = int(input("¿Cuántos números va a ingresar?: "))

suma_pares = 0
suma_impares = 0

for i in range(N):
    numero = int(input("Ingrese un número: "))

    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print("Suma de pares:", suma_pares)
print("Suma de impares:", suma_impares)