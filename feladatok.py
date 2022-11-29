
haromal=[]
for i in range(1,40):
    if i %3==0:
        haromal.append(i)
print(haromal)

#2
t_kezd=[]
szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
for i in szavak:
    if i.startswith("T") or i.startswith("t"):    
        print (i)
        t_kezd.append(i)
print(t_kezd)

#3
szamok = [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57]
for i in szamok:
    if i %3==0:
        if i %2==0:
            print(i)
