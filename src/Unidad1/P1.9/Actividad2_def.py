def importeTotal(horas, coste):
    return horas * coste

horas = int(input("Horas de trabajo: "))
coste = float(input("Coste por hora: "))
print(f"El importe total es de {importeTotal(horas, coste)}")