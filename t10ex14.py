def gran():
    print("Hola, este programa lo que hace es pedirte 2 numeros, y luego, decirte el numero mayor, pruebalo!")
    numero1=int(input("Introduzca su primer número: "))
    numero2=int(input("Introduzca su segundo número: "))
    if numero2 < numero1:
        print("El número más grande es {}".format(numero1))
    elif numero2>numero1:
        print("El número más grande es {}".format(numero2))
    else:
        print("Los 2 números son iguales")
gran()