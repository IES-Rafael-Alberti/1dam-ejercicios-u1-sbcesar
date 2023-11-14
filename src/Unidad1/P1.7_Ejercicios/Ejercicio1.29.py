# Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que solicite un nombre y una edad.
#   - Si el nombre está vacío, debes utilizar el valor "Desconocido". 
#     La edad debe pedirla hasta que introduzca una edad comprendida entre 0 y 125 años.
#   - El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".
#   - El pseudocódigo debes incluirlo como comentarios en el programa de Python.
#----------------------------------------------------------------------------------------------------------------------

# PSEUDOCODIGO
# ----------------
# Leer nombre
# Leer edad

# Si nombre == null entonces
#     nombre = "Desconocido"

# Mientras edad > 0 and edad < 125 entonces
#     resto = 125 - edad
#     Imprimir "Te llamas" + nombre + " y tienes" + edad + "años, te quedan aún" + resto + "años por cumplir"
# Si no entonces
#     Imprimir "Error - Introduce una edad correcta"

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

if nombre == "":
    nombre = "Desconocido"

while edad > 0 and edad < 125:
    resto = 125 - edad
    print(f"Te llamas {nombre} y tienes {edad} años, te quedan aún {resto} años por cumplir")
    break
else:
    print("Error - Introduce una edad correcta")