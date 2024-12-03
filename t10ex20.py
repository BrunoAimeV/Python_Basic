def invertir(s):
    return s[::-1]

def es_palindrom(s):
    if s == invertir(s):
        return True
    else:
        return False

s=input("Introdueix una cadena: ")
a=invertir(s)
if es_palindrom(s):
    print(f"La frase/paraula {s} es igual a {invertir(s)} i, per tant, es palindrom")
else:
    print(f"La frase/paraula es {s} no és igual a {a} i, per tant, no es palindrom")