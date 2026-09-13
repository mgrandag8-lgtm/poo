edad = int(input("Ingrese su edad: "))

while edad < 0 or edad > 120:
    print("Edad inválida")
    edad = int(input("Ingrese su edad nuevamente: "))

print("Edad válida:", edad)