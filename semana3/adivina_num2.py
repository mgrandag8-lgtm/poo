import random

secreto = random.randint(1, 100)
intentos = 0
numero = 0

while numero != secreto:
    numero = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1

    if numero < secreto:
        print("El número secreto es mayor")

    elif numero > secreto:
        print("El número secreto es menor")

    else:
        print("¡Adivinaste!")

print("Número de intentos:", intentos)