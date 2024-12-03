import time


# Calculadora python
def menu():
    print("\nCalculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Resto división")
    print("6. Cociente divisor")
    print("7. Potencia")
    print("8. Canvis de base (binari, octal, decimal, hexadecimal)")
    print("9. Salir")
    a = int(input("Introduzca una opción: "))
    return a


def Sumar():
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el número por el que lo vas a sumar: "))
    return numero1 + numero2


def Restar():
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el número por el que vas a restar: "))
    return numero1 - numero2


def Multiplicar():
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el número por el que vas a multiplicar: "))
    return numero1 * numero2


def Dividir():
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el número divisor: "))
    if numero2 != 0:
        return numero1 / numero2
    else:
        return "Error: No se puede dividir por cero."


def Resto():
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el número divisor: "))
    if numero2 != 0:
        return numero1 % numero2
    else:
        return "Error: No se puede dividir por cero."


def Cociente():
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el divisor: "))
    if numero2 != 0:
        return numero1 // numero2
    else:
        return "Error: No se puede dividir por cero."


def Potencia():
    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el número por el que lo vas a elevar: "))
    return numero1 ** numero2


def canvis_de_base():
    while True:
        print("\nCanvis de Base")
        print("1. Decimal a Binari")
        print("2. Decimal a Octal")
        print("3. Decimal a Hexadecimal")
        print("4. Binari a Decimal")
        print("5. Octal a Decimal")
        print("6. Hexadecimal a Decimal")
        print("7. Tornar al menú principal")
        op = int(input("Selecciona una opció: "))

        if op == 1:
            numero = int(input("Introduce un número decimal: "))
            print(f"El número {numero} en binari és: {bin(numero)[2:]}")
        elif op == 2:
            numero = int(input("Introduce un número decimal: "))
            print(f"El número {numero} en octal és: {oct(numero)[2:]}")
        elif op == 3:
            numero = int(input("Introduce un número decimal: "))
            print(f"El número {numero} en hexadecimal és: {hex(numero)[2:].upper()}")
        elif op == 4:
            numero = input("Introduce un número binari: ")
            print(f"El número {numero} en decimal és: {int(numero, 2)}")
        elif op == 5:
            numero = input("Introduce un número octal: ")
            print(f"El número {numero} en decimal és: {int(numero, 8)}")
        elif op == 6:
            numero = input("Introduce un número hexadecimal: ")
            print(f"El número {numero} en decimal és: {int(numero, 16)}")
        elif op == 7:
            print("Tornant al menú principal...")
            break
        else:
            print("Opció no vàlida.")
        time.sleep(2)


# Bucle principal
b = True
while b:
    a = menu()
    match a:
        case 1:  # Sumar
            resultado = Sumar()
            print(f"Resultado de la suma: {resultado}")
        case 2:  # Restar
            resultado = Restar()
            print(f"Resultado de la resta: {resultado}")
        case 3:  # Multiplicar
            resultado = Multiplicar()
            print(f"Resultado de la multiplicación: {resultado}")
        case 4:  # Dividir
            resultado = Dividir()
            print(f"Resultado de la división: {resultado}")
        case 5:  # Resto
            resultado = Resto()
            print(f"Valor restante de la división: {resultado}")
        case 6:  # Cociente
            resultado = Cociente()
            print(f"Cociente de la división: {resultado}")
        case 7:  # Potencia
            resultado = Potencia()
            print(f"Resultado de la potencia: {resultado}")
        case 8:  # Canvis de base
            canvis_de_base()
        case 9:  # Salir
            print("Adiós")
            b = False
        case _:  # Opción no válida
            print("Opción no válida, por favor, introduzca un número del menú principal")

    time.sleep(2)
