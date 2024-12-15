def llegir_llista():
   l = []
   a = "a"
   while a!= ".":
       a = input("Introdueix una paraula (o escriu '.' per acabar): ")
       if a!= ".":
           l.append(a)
   return l


def index_paraula(l,paraula):
   if paraula not in l:
       return -1
   else:
       for i,e in enumerate(l):
           if e==paraula:
               return i
          
l=llegir_llista()
p=input("Dir quina paraula de la llista vols cercar: ")
n=index_paraula(l,p)
if n>0:
   print(f"La paraula {p} esta en la posició {n}")
else:
   print("La paraula no esta dins la llista")
