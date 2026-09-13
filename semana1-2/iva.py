precio = float(input("Ingrese el precio: "))

iva = precio * 0.15
total = precio + iva

print(f"IVA: ${iva}")
print(f"Total con IVA: ${total}")