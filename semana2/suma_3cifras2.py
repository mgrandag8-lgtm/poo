numero = int(input("Ingrese un número de 3 cifras: "))

centena = numero // 100
decena = (numero // 10) % 10
unidad = numero % 10

suma = centena + decena + unidad

print("La suma de los dígitos es:", suma)