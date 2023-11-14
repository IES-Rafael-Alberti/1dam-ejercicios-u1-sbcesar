
def precioFinal(importe, iva):
    importe = importe * (iva / 100)
    print(f"El precio final del producto es {importe}")

importe = float(input("Introduce el precio del producto (sin iva): "))
iva = int(input("Introduce el IVA a aplicar: "))
precioFinal(importe, iva)