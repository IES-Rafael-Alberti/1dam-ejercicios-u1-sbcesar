def operacion(n):
    
    suma = (n*(n+1))/2
    return f"La suma de los enteros desde 1 hasta {n} es {suma}."

n = int(input("Introduce un numero entero positivo: "))
print(operacion(n))


