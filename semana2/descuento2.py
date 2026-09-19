precio = 12

cantidad = int(input("Ingrese la cantidad de productos: "))

subtotal = precio * cantidad

if cantidad >= 10:
    descuento = subtotal * 0.15

elif cantidad >= 5:
    descuento = subtotal * 0.05

else:
    descuento = 0

total = subtotal - descuento

print("Subtotal:", subtotal)
print("Descuento:", descuento)
print("Total:", total)