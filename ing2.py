def ing(meret):
    if meret<40:
        return 'Fiatal'
    elif meret>40 and meret <45:
        return 'Középkorú'
    else:
        return 'Idős'

nev=None

while nev!='':
    nev=input('Adja meg a nevét')
    if nev:
        meret=int(input('Adja meg a méretét'))
        if ing(meret):
            print(f'{nev} {meret}')
    else:
        break