

pénz=int(25000)
tipus=input("Add meg a gép tipusát. ")
müköd=input("Müködik a gép?(igen/nem) ")
ár=int(input("mennyibe kerül? "))
feltételek=0

if tipus=="c64" or tipus=="ZX":
    feltételek+=1

if müköd=="igen":
    feltételek+=1

if ár<pénz:
    feltételek+=1

if feltételek==3:
    print("megveszük")
elif feltételek<3:
    print("nem vesszük meg")
