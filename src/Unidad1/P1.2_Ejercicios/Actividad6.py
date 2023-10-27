importeFinal = float(input("Introduce el precio final del producto: "))

precioIva = importeFinal / 0.1

importeSinIva = importeFinal - precioIva

print("Precio final del producto: ", importeFinal)
print("Precio del iva introducido (10%): ", precioIva)
print("Precio del producto sin IVA: ", importeSinIva)