nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
nUnidades = int(input("Introduce la cantidad: "))
costeTotal = nUnidades * precio

precio = "{:6.2f}".format(precio)
nUnidades = "{:03d}".format(nUnidades)
costeTotal = "{:8.2f}".format(costeTotal)

print(f"Nombre: {nombre}\nPrecio: {precio}\nUnidades: {nUnidades}\nPrecio final: {costeTotal}")

