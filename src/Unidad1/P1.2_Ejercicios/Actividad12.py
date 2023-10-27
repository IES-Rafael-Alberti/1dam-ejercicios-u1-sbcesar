peso = float(input("Introduce tu peso(KG): "))
estatura = float(input("Introduce tu estatura(m): "))

indice = peso / (estatura**2)

print(f"Tu índice de masa corporal es {round(indice, 2)}")