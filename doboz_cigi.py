def doboz(szál):
    doboz=szál/20
    return doboz

def bagó():
    if doboz>2:
        return 'Nagy dohányos'
    else:
        return 'Kis dohányos'

nev=None
while True:
    if nev!='':
        nev=input('Adja meg a nvét! ')
        szal=int(input('Adj meg hogy mennyit szív! '))
        if doboz(szal):
            print(nev,bagó(doboz(szal)))
        else:
            print(nev,bagó(doboz(szal)))
    else:
        break
