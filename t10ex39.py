x=int(input("Quantitat: "))
i=float(input("interés: "))
a=int(input("Numero d'anys: "))
c=x+((1+i/100)**a)
print(f"Els {x}€ Demanats, amb un interés del {i}% en {a} anys, es convertirá al final en {c}€")