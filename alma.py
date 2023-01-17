


nev=None
szam=None
while nev!='':
    nev=input('Add meg a vásárló nevét! ')
    if nev=='':
        break
    szam=int(input('Add meg a gyümölcs vonalkódjának első három számát ! '))

    if szam==599:
        print(nev,' magyar gyümölcsöt vásárolt')
    elif szam==600:
        print(nev,'nem magyar gyümölcsöt vásárolt.')
    
