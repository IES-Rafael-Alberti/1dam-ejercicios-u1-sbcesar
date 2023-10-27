dinero = float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: "))

interes = 0.04

anos = 3

for ano in range(1, anos +1):
    saldo = dinero * (1 + interes) ** ano
    print(f"Saldo después del año {ano}: {round(saldo, 2)}")
