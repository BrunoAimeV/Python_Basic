x=int(input("Introdueix un numero menor de 100: "))
y=0.0
for i in range(x,1,-4):
    y+=i**2
print(f"la suma dels cuadtas de 4 en 4 de {x} és {y}")