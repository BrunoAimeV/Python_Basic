import random

def llista_20_elements():
    l=[]
    for i in range(20):
        l.append(random.randint(1,100))
    return l
l=llista_20_elements()
print(l)