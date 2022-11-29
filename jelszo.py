
bejutott=False
while not bejutott:
    felhasznalonev=input('kéram adja meg a felhasználónevét ')
    jelszo=input('kéram adja meg a jelszavát ')
    if felhasznalonev=='bori99'and jelszo=='kismehe<3':
        print('a belépés megengedve')
        bejutott=True
    else:
        print('belépés megtagadva')