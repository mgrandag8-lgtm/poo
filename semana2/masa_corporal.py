peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

imc = peso / (estatura ** 2)

print(f"Su IMC es: {imc:.2f}")