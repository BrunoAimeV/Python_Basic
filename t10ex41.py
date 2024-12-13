def comptar_digits(numero):
    if 1 <= numero <= 900000:
        return len(str(numero))
    else:
        return "El número ha d'estar entre 1 i 900000."

numero = int(input("Introdueix un número (entre 1 i 900000): "))
resultat = comptar_digits(numero)
print(f"El número té {resultat} dígits.")
