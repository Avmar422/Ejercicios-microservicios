Producto= input("Inserte producto:")
Cantidad= int(input("Inserte cantidad:"))
Precio= float(input("Inserta el precio:"))

Total= (Precio*Cantidad)

print(f"Venta de {Producto}:{Cantidad} unidades a un precio de ${Precio}")
print(f"Total: ${Total}")