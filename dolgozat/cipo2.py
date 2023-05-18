def nagy_v_kis(méret):
    if méret>=41:
        return True
    else:
        return False

nev=None
while nev!='':
    nev=input('Add meg a cipőt használó nevét! ')
    if nev=='':
        break
    méret=int(input('Add meg a pontszámát!'))
    if nagy_v_kis(méret)==True:
        print(f'{nev} nagy lábon él. ')
    else:
        print(f'{nev} kis lábon él. ')