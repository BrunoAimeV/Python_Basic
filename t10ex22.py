def crear_repetició(n,c):
    return c*n

a=input("Introdueix un caracter: ")
b=int(input("Introdueix les vegades que vols repetir el caracter: "))
print(f"El caracter {a} repetit {b} vegades és {(crear_repetició(b,a))}")