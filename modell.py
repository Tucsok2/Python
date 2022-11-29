'''
megfelel=False
nev=input('Mi a neve? ')
magasag=int(input('Milyen magas? '))
while nev!='':
    if magasag>=170:
        megfelel=True
    if megfelel==True:
        print(nev,'megefelü magasságú.')
        magasag=int(input('Milyen magas? '))
    else:
        print(nev,'magassága nem megfelelő modellnek.')
    nev=input('Mi a neve? ')
'''
   
def megfelel(m):
    if int(m)<170:
        return False
    else:
        return True

nev=None
while nev !='':
    nev=input('Mi a neve? ')
    if nev!='':
        m= input('Milyen magas? ')
        if megfelel(m):
            print(nev,'megefelü magasságú.')
        else:
            print(nev,'magassága nem megfelelő modellnek.')