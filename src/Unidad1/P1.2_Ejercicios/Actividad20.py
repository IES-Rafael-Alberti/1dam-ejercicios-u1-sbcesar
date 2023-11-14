cadena = input("Introduce tu numero de teléfono con este formato (+XX-XXXXXXXXX-XX): ")

pos1 = cadena.find("-")
pos2 = cadena.find("-", pos1 + 1)

prefijo = cadena[:pos1]
numero = cadena[pos1+1:pos2]
extension = cadena[pos2+1:]

print(f"Su número de teléfono es {numero}")
        