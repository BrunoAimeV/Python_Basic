import random

def crear_numero():
    l=[]
    for i in range(4):
        l.append(random.randint(0,9))
    return l
def comprarar(l):
    s=[]
    r=[0, 0, 0, 0]
    for i in range(4):
        s.append(int(input("Introdueix el codi: ")))
        if l[i]==s[i]:
            r[i]=2
    for i,e in enumerate(s):
        if e in l and r[i]!=2:
            r[i]=1

m=crear_numero()

print(m)