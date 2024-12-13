def llegir_llista():
    l=[]
    print("Introdueix paraules per crear una llista. Escriu '.' per acabar.")
    a="a"
    while a!=".":
        a=input("Introdueix una paraula:")
        if a!=".":
            l.append(a)
    return l

def paraula_mes_llarga(l):
    a=l[0]
    for e in l:
        if len(e) > len(a):
            a=e
    return a
a=llegir_llista()
print(f"la paraula més llarga de la llista és: {paraula_mes_llarga(a)}")