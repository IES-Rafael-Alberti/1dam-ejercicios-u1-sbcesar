def conversion():
    fahrenheit = float(input("Introduce los grados Fahrenheit: "))
    fahrenheit = (fahrenheit - 32) *5 / 9
    return round(fahrenheit, 2)

print(conversion())