producto = float(input("Introduce el precio del producto (sin iva): "))
iva = int(input("Introduce el IVA a aplicar: "))

precioFinal = producto * (iva / 100)

print("El precio final del producto es {:.2f}".format(precioFinal))