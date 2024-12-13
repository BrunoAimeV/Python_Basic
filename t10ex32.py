def llegir_llista():
    l = []
    a = "a"
    while a != ".":
        a = input("Introdueix un nom (o escriu '.' per acabar): ")
        if a != ".":
            l.append(a)
    return l

def noms_que_comencen_per_a(llista):
    noms_filtrats = [nom for nom in llista if nom.lower().startswith('a')]
    return len(noms_filtrats), noms_filtrats

# Programa principal
noms = llegir_llista()

quantitat, noms_comencen_per_a = noms_que_comencen_per_a(noms)

print(f"Hi ha {quantitat} noms que comencen per la lletra 'a'.")
if noms_comencen_per_a:
    print("Els noms són:", ", ".join(noms_comencen_per_a))
else:
    print("No hi ha noms que comencin per la lletra 'a'.")
