def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un numero: ")
        if a!=".":
            l.append(int(a))
    return l

def gran_llista(l):
    return max(l)
a=llegir_llista()
print(f"El major de la llista és {gran_llista(a)}")