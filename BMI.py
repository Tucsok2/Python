


listas = []
listam = []
for i in range(3):
    s = float(input('Hány kiló vagy? '))
    listas.append(s)
    m = float(input('Milyen magas vagy? '))
    listam.append(m)
    m = m/100
    bmi = s/m**2
    if bmi <= 18.49:
        print('Sovány')
    elif bmi <= 24.99:
        print('Normális testsúly')
    else:
        print('Túlsolyos')
    print(bmi)

    print('')
    

"""
átlag=0
össz_s=0
for i in enumerate(listas):
    össz_s=össz_s+1
    átlag=össz_s/len(listas)
    print(össz_s)
    print(átlag)
"""

print(listas)
print(listas.sort)
print(listas.reverse)
print(listas.index(2))