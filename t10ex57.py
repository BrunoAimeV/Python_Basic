def llegir_llista():
    l = []
    a = "a"
    while a!= ".":
        a = input("Introdueix una paraula (o escriu '.' per acabar): ")
        if a!= ".":
            l.append(a)
    return l

def elements_parells(l):
    print(l[::2])

l=llegir_llista()
elements_parells(l)