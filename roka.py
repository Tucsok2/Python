



'''
ketrec = [2, 4, 7, 9, 8, 5, 4, 3]
megszamol_tomeg = 0
osszeg = 0
for num in ketrec:
    osszeg = osszeg+num
alen = len(ketrec)
print('összes liba: ',len)
print('összesen a libák tömege: ',osszeg)
elvitt = 0
for i in ketrec:
    if i > 5:
        megszamol_tomeg = megszamol_tomeg+1
        elvitt += 1
        ketrec.remove(i)
print('elvitt libák száma: ', elvitt)
print('elvitt libák tömege: ', megszamol_tomeg)
átlag = osszeg/alen
print('elvitt libák tömegének átlaga',átlag)
újab=[4,7,8,6,5,3]
for i in újab:
    ketrec.insert(1,i)



ketrec_új=ketrec
megszamol_tomeg2 = 0
osszeg2 = 0
for num in ketrec_új:
    osszeg2 = osszeg2+num
alen2=len(ketrec_új)
print('újakkal összes liba: ',alen2)
print('az újakkal  összes libák tömege: ',osszeg2)
elvitt2 = 0
for i in ketrec_új:
    if i > 5:
        megszamol_tomeg2 = megszamol_tomeg2+1
        elvitt2 += 1
        ketrec.remove(i)
print('elvitt libák száma: ', elvitt)
print('elvitt libák tömege: ', megszamol_tomeg)
átlag2 = osszeg2/alen2
print('elvitt libák tömegének átlaga',átlag2)
'''

szélsőérték=(max,min)
t=[2,5,6,9,10,12,4]
maxElem=t[0]
for elem in t:
    if elem>maxElem:
        maxElem=elem
print(maxElem)

minElem=t[0]
for elem in t:
    if elem<minElem:
        minElem=elem
print(minElem)

