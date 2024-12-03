# Definir una función que conti la longitud
def llegir_llista():
    l=[]
    a=""
    while a!=".":
        a=input("Indroduce un numero de la lista: ")
        if a!=".":
            l.append(int(a))
        return l
def longitud(l):
    return len(l)

#programa principal
x = llegir_llista()
print(longitud(x))