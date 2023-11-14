n1 = int(input("Introduce un numeros: "))
n2 = int(input("Introduce otro numeros: "))

opcion = 0

while opcion < 1 or opcion > 4:
    opcion = int(input("Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División): "))
    if opcion < 1 or opcion > 4:
        print("Error - No es una opción correcta (1-4)")

match opcion:
    case 1:
        print(f"{n1} + {n2} = {n1+n2}")
    case 2:
        print(f"{n1} - {n2} = {n1-n2}")
    case 3:
        print(f"{n1} * {n2} = {n1*n2}")
    case 4:
        if n2 == 0:
            print("La división por cero no es posible")
        else:
            print(f"{n1} / {n2} = {n1/n2}")