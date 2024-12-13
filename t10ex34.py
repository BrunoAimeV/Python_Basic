def comptar_vocals(p):
    ap=[0,0,0,0,0]
    for e in p:
        if e=="a" or e=="A":
            ap[0]+=1
        elif e=="e" or e=="E":
            ap[1]+=1
        elif e=="i" or e=="I":
            ap[2]+=1
        elif e=="o" or e=="O":
            ap[3]+=1
        elif e=="u" or e=="U":
            ap[4]+=1
        else:
            print(f"{e} no es una vocal")
    print(f"La vocal a apareix {ap[0]} vegades, la e {ap[1]} vegades, la i {ap[2]} vegades, la o {ap[3]} vegades i la u {ap[4]} vegades")

x=input("Introduir paraula: ")
comptar_vocals(x)