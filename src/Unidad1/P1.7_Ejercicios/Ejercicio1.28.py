# Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que lea dos números enteros,
# muestre cuál es el menor de los dos y cuantos números existen entre ellos dos.
#   - El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
#   - Si los números son diferentes, por ejemplo 5 y 12 debe mostrar la frase "El número menor es el 5 y entre 
#     ellos existen 7 números enteros".
#   - El pseudocódigo debes incluirlo como comentarios en el programa de Python.
#------------------------------------------------------------------------------------------------------------------

# PSEUDOCÓDIGO
# -------------------------
# Leer num1
# Leer num2
# Si num1 < num2 entonces
#   operacion = num2 - num 1
#   Imprimir "El numero menor es el " + num1 + " y entre ellos existen " + operacion + " numeros enteros"
# Si num1 > num2 entonces
#   operacion = num1 - num2
#   Imprimir "El numero menor es el " + num2 + " y entre ellos existen " + operacion + " numeros enteros"
# Si no entonces
#   Imprimir "Los numeros no pueden ser iguales"

num1 = float(input("Introduce un numero: "))
num2 = float(input("Introduce otro numero: "))

if num1 < num2:
    operacion = num2 - num1
    print(f"El numero menor es el {num1} y entre ellos existen {operacion} numeros enteros")
elif num1 > num2:
    operacion = num1 - num2
    print(f"El numero menor es el {num2} y entre ellos existen {operacion} numeros enteros")
else:
    print("Los números no pueden ser iguales")