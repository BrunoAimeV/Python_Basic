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
   print("8. Salir")
   a =int(input("Introduzca una opción: "))
   return a
def Sumar():
   numero1=int(input("introduce el primer numero: "))
   numero2=int(input("introduce el numero por el que lo vas a sumar: "))
   return numero1 + numero2
def Restar():
   numero1=int(input("introduce el priemr numero: "))
   numero2=int(input("introduce el numero por el que vas a restar: "))
   return numero1 - numero2
def Multiplicar():
   numero1=int(input("introduce el primer numero: "))
   numero2=int(input("introduce el numero por el que vas a multiplicar: "))
   return numero1 * numero2
def Dividir():
   numero1=int(input("introduce el primer numero: "))
   numero2=int(input("introduce el numero divisor: "))
   return numero1 / numero2
def Resto():
   numero1=int(input("Introduce el primer numero:"))
   numero2=int(input("introduce el numero divisor: "))
   return numero1 % numero2
def Cociente():
   numero1=int(input("introduce el primer numero: "))
   numero2=int(input("introduce el divisor: "))
   return numero1 // numero2
def Potencia():
   numero1=int(input("introduce el primer numero: "))
   numero2=int(input("introduce el numero por el que lo vas a elevar: "))
   return numero1 ** numero2


b = True
while b:
   a = menu()
   match a:
       case 1:  # 1. Sumar
           resultado = Sumar()
           print(f"Resultado de la suma: {resultado}")
       case 2:  # 2. Restar
           resultado = Restar()
           print(f"Resultado de la resta: {resultado}")
       case 3:  # 3. Multiplicar
           resultado = Multiplicar()
           print(f"Resultado de la multiplicación: {resultado}")
       case 4:  # 4. Dividir
           resultado = Dividir()
           print(f"Resultado de la división: {resultado}")
       case 5:  # 5. Resto
           resultado = Resto()
           print(f"Valor restante de la división: {resultado}")
       case 6:
           resultado = Cociente()
           print(f"Cociente de la división: {resultado}")
       case 7:
           resultado = Potencia()
           print(f"Resultado de la potencia: {resultado}")


       case 8: # 6. Salir
           print("Adiós")
           b = False
       case _:  # Opción no válida
           print("Opción no válida, por favor, introduzca un número del menú principal")


   time.sleep(3)