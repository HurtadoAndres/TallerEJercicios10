n1 = int(input("Introduce numero1: "))
n2 = int(input("Introduce  numero2: "))

if n1 < n2:
    numero2 = n2 +1
    for resul in range(n1, (numero2)):
        if resul%2 == 0:
            print(f"Es par {resul} ")
        else:
            print(f"Es impar {resul} ")

else:
    print("El numero 1 debe ser mayor que el numero 2")
