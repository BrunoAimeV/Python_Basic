def llista_fitxer(nom):
    l=[]
    with open(nom,"r") as f:
        for line in f:
            l.append(line)
        return l

l=llista_fitxer("prova1.txt")
print(l)