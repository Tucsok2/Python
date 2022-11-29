szo1=input('kérem adja meg szo1 ')
szo2=input('kérem adja meg szo2 ')
szo1_van=szo1.find('e')
szo2_van=szo2.find('e')

szo1_van=szo1(szo1[0])


if szo1_van>0 and szo2_van>0:
    print('oké')
else:
    print('nem jó')