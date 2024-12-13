def llegir_llista():
    l = []
    a = "a"
    while a!= ".":
        a = input("Introdueix un numero (o escriu '.' per acabar): ")
        if a!= ".":
            l.append(a)
    return l

def eliminar_duplicats(l):
    s =set(l)
    return list(s)

l=llegir_llista()
r=eliminar_duplicats(l)
print(f"La llista queda així {r}")