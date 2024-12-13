def llegir_llista():
    l = []
    a = "a"
    while a!= ".":
        a = input("Introdueix un nom (o escriu '.' per acabar): ")
        if a!= ".":
            l.append(a)
    return l

def retorna_nova_llista(l):
    return l[1:-1]

l=llegir_llista()
s=retorna_nova_llista
print(f"{l} es transforma en {s}")