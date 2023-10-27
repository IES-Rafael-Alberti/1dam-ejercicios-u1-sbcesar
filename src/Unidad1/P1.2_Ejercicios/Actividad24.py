precio = float(input("Introduce el precio del producto(€) con dos decimales: "))

precioStr = '{:.2f}'.format(precio)
euros, centimos = precioStr.split('.')

print(f"Euros: {euros}\nCéntimos: {centimos}")