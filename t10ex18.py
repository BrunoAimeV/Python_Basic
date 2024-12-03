def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l

def sumar_llista(l):
    suma=0
    for e in l:
        suma+=e
    return suma

def multiplicar_llista(l):
    multiplicacio=1
    if 0 in l or len(l)==0:
        return 0
    else:
        for e in l:
            multiplicacio *= e
    return multiplicacio

# Programa principal
l=llegir_llista()
print(f"la suma dels elements de la llista {l} és {sumar_llista(l)}")
print(f"la multiplicació dels elements de la llista {l} és {multiplicar_llista(l)}")