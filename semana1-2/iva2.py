precio = float(input("Ingrese el precio: "))

iva = precio * 0.15
total = precio + iva

print(f"IVA: ${iva:.2f}")
print(f"Total con IVA: ${total:.2f}")
