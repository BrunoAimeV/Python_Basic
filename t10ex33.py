def llegir_llista():
    l = []
    a = "a"
    while a != ".":
        a = input("Introdueix noms (o escriu '.' per acabar): ")
        if a != ".":
            l.append(a)
    return l

def noms_que_comencen_per(llista, lletra):
    lletra = lletra.lower()
    noms_filtrats = [nom for nom in llista if nom.lower().startswith(lletra)]
    return len(noms_filtrats), noms_filtrats

# Programa principal
noms = llegir_llista()
lletra = input("Introdueix la lletra per la qual han de començar els noms: ").strip()

quantitat, noms_comencen_per = noms_que_comencen_per(noms, lletra)

print(f"Hi ha {quantitat} noms que comencen per la lletra '{lletra}'.")
if noms_comencen_per:
    print("Els noms són:", ", ".join(noms_comencen_per))
else:
    print("No hi ha noms que comencin per aquesta lletra.")