



nevek=[]
láz=[]
for i in range(3):
    név=input('kérem adja meg nevét. ')
    nevek.append(név)
    fok=float(input('Mennyi a testhőmérséklette? '))
    láz.append(fok)
    if fok<=37:
        print('Normális')
    elif fok<=35.5:
        print('Ki vagy hülve')
    elif fok>37 and fok<=38:
        print('hőemelkedés')
    else:
        print('Magas láz')

print(nevek)
print(láz)