def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l

def mostrar_majors_que(t, num):
    for e in t:
        if e>num:
            print("{} és major que {}".format(e, num))
    

#Programa principal
x = llegir_llista()
y = tuple(x)
num=int(input("Introdueixi el número a comparar: "))
mostrar_majors_que(y, num)


def llegir_llista():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un número: ")
        if a!=".":
            l.append(int(a))
    return l

def mostrar_majors_que(t, min, max):
    for e in t:
        if e>min and e<max:
            print("{} és major que {} i menor que {}".format(e, min, max))
    

#Programa principal
x = llegir_llista()
y = tuple(x)
min=int(input("Introdueixi el número a comparar menor: "))
max=int(input("Introdueixi el número a comparar major: "))
mostrar_majors_que(y, min, max)