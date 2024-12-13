def es_de_traspas(any):
    if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
        return True
    else:
        return False

any = int(input("Introdueix l'any on som: "))

if es_de_traspas(any):
    print(f"{any} és un any de traspàs.")
else:
    print(f"{any} NO és un any de traspàs.")
