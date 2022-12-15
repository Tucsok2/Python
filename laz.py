def laz(hom):
    if hom>37.5:
        return True
    else:
        return False
    
nev=None
while nev!='':
    nev=input('kérem adja meg a nevét! ')
    if nev:
        hom=float(input('kérem adja meg a hömérsékletét! '))
        if laz(hom):
            print(f'{nev} lázas')
        else:
            print(f'{nev} nem lázas')