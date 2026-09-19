def suma(x, y):
    resultado = x + y
    return resultado


def resta(x, y):
    resultado = x - y
    return resultado


def producto(x, y):
    resultado = x * y
    return resultado


def division(x, y):
    if y == 0:
        return "Error, no se puede dividir entre cero"
    return x / y


print("CALCULADORA")
print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicación")
print("4 - División")

eleccion = int(input("Ingrese una opción: "))

num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

if eleccion == 1:
    respuesta = suma(num1, num2)
elif eleccion == 2:
    respuesta = resta(num1, num2)
elif eleccion == 3:
    respuesta = producto(num1, num2)
elif eleccion == 4:
    respuesta = division(num1, num2)
else:
    respuesta = "Opción incorrecta"

print("Resultado:", respuesta)