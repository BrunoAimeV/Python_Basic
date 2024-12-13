a = 2024
d = []
l = []

for i in range(4):
    nom = input("Indica el teu nom: ")
    any_naixement = int(input("Indica l'any que vas néixer: "))
    d = [nom, any_naixement]
    l.append(d)

print("\t nom \t Data naixement \t Anys que farà aquest any")
for e in l:
    anys = a - e[1]
    print("{:<20} {:<20} {:<20}".format(e[0], e[1], anys))
