x=input("Introdueix un numero: ")
sum=0
for e in x:
    sum+=int(e)
if sum%2==0:
    print(f"la suma dels digits del numero {x} és {sum} i es parell")
else:
    print(f"la suma dels digits del numero {x} és {sum} i es senar")