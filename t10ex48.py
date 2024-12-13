def llegir_llista():
    l = []
    a = "a"
    while a!= ".":
        a = input("Introdueix un nom (o escriu '.' per acabar): ")
        if a!= ".":
            l.append(a)
    return l

def hi_ha_duplicats(l):
    s = set(l)
    if len(l)==len(s):
        print("No hu ha duplicats")
    else:
        print("Hi ha duplicats")

l=llegir_llista
hi_ha_duplicats(l)