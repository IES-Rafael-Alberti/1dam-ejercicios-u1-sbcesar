x = int(input("Introduce un numero: "))
y = int(input("Introduce otro numero: "))

if x <= y:
    numIni = x
    numFin = y
else:
    numIni = y
    numFin = x

for i in range(numIni, numFin):
    print(i, end="-")

print(numFin)