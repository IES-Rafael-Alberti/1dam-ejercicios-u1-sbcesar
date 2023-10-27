total = int(input("¿Cuántas notas vas a introducir? "))

while total < 1 or total > 100:
    print("Error - el número de notas debe ser un número entero entre 1 y 100")
    total = int(input("¿Cuántas notas vas a introducir?"))

media = 0
cont = 1

while cont <= total:
    nota = float(input(f"Dame las {total} notas del curso: "))
    media = media + nota
    cont += 1

media = media / total
print("La media es ", media)