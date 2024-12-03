def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número")
        if a!=".":
            l.append(int(a))
    return l

def superpisició():