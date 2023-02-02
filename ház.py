def oldal(házszám):
    if házszám%2==0:
        return True
    else:
        return False
    
utca=None
házszám=None
while utca!='':
    utca=input('Add meg az utca nevét! ')
    if utca=='':
        break
    házszám=int(input('Add meg a házszámot! '))
    if oldal(házszám)==True:
        print('A ház a jobb oldalon van.')
    else:
        print('A ház a bal oldalon van')