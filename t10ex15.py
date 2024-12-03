def gran_de_tres():
    print("Hola, este programa lo que hace es pedirte 3 numeros, y luego, decirte el numero mayor, pruebalo!")
    numero1 = int(input("Introduzca su primer número: "))
    numero2 = int(input("Introduzca su segundo número: "))
    numero3 = int(input("Introduzca su tercer número: "))
    
    if numero1 == numero2 == numero3:
        print("Los 3 números son iguales.")
    elif numero1 >= numero2 and numero1 >= numero3:
        print("El número más grande es: {}".format(numero1))
    elif numero2 >= numero1 and numero2 >= numero3:
        print("El número más grande es: {}".format(numero2))
    else:
        print("El número más grande es: {}".format(numero3))
gran_de_tres()