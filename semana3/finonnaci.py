N = int(input("¿Cuántos números de Fibonacci desea mostrar?: "))

a = 0
b = 1

for i in range(N):
    print(a)

    siguiente = a + b
    a = b
    b = siguiente