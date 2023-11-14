# Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que pida un número de inicio,
# un incremento y un total de la serie.
#   - El incremento y el total deben ser mayor que cero, sino el programa debe finalizar con un error 
#   u obligar a que introduzcan un valor correcto de ambos (os lo dejo a vuestra elección, 
#   la primera opción es más fácil, aunque el mundo está lleno de valientes)
#   - Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo 
#   siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
#   - El pseudocódigo debes incluirlo como comentarios en el programa de Python.
#---------------------------------------------------------------------------------------------------------

# PSEUDOCODIGO
#----------------
# Leer num
# Leer incremento
# Leer totalSerie

# Mientras incremento < 0 and totalSerie < 0 entonces
#     Imprimir "Por favor, introduce un valor correcto"
# Si no entonces
#     Para i en num..totalSerie+1 entonces
#         incremento += incremento
#         Imprimir i

num = int(input("Introduce el numero inicial de la serie: "))
incremento = int(input("Introduce los saltos de la serie: "))
totalSerie = int(input("Introduce el numero final de la serie: "))

while incremento < 0 or totalSerie < 0:
    print("Por favor, introduce un valor correcto")
    incremento = int(input("Introduce los saltos de la serie: "))
    totalSerie = int(input("Introduce el numero final de la serie: "))

print("Serie => ", end=str(num) + "-")
cont = 1
while (cont < totalSerie):
    num += incremento
    cont += 1
    if cont < totalSerie-1:
        print(num, end="..")
    elif cont == totalSerie:
        print(num, end="")
    else:
        print(num, end="-")

    