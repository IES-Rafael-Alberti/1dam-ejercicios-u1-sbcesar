fecha = input("Introduce tu fecha de nacimiento (DD/MM/YYYY): ")

dia, mes, ano = fecha.split("/")

if len(dia) == 1:
    dia = "0" + dia
if len(mes) == 1:
    mes = "0" + mes

print(f"Día: {dia}, Mes: {mes}, Año: {ano}")