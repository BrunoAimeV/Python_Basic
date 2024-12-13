# Palabras que riman
def comprobar_rima(palabra1, palabra2):
    if palabra1[-3:] == palabra2[-3:]:
        return "Rimen"
    elif palabra1[-2:] == palabra2[-2:]:
        return "Rimen un poc"
    else:
        return "No rimen"

palabra1 = input("Introdueix la primera paraula: ")
palabra2 = input("Introdueix la segona paraula: ")

print(comprobar_rima(palabra1, palabra2))