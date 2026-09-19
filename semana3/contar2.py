numero = int(input("Ingrese un número: "))

numero = abs(numero)

if numero == 0:
    digitos = 1
else:
    digitos = 0

    while numero > 0:
        numero = numero // 10
        digitos += 1

print("Cantidad de dígitos:", digitos)