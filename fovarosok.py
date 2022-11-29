import random


fovarosok=[]
fovarosok=["Bécs",'Bern',"Párisz","London","Budapest","Varsó","Prága","Róma","Madrid","Helsinki","Moszkva"]
fváros=None
while fváros!="":
    print("fővárosok jelenleg",", ".join(fovarosok))
    fváros=input("Kérek egy fővárost! ")
    if fváros!=" ":
        fovarosok.append(fváros)

for index, főváros in enumerate(fovarosok):
    print(index,főváros)

while len(fovarosok)>0:
    print("fővárosaink",", ".join(fovarosok))
    melyik=input("Melyik főváros a legszebb, válaszd ki! ")
    if melyik in fovarosok:
        fovarosok.remove(melyik)
    else:
        print("Ilyen város nincs a listába")