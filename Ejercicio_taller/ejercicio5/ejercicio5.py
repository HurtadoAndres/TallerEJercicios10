numero1 = int(input("Introduce  número1: "))
numero2 = int(input("Introduce  número2: "))

if numero1 < numero2:

    for contador in range(numero1, (numero2 + 1)):
        print(contador)

else:
    print("numero 1 debe ser menor que el numero 2 para poder operar")