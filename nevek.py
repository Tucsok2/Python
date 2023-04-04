wr=open('H:\masodik\python/nevek.txt','r')
asok=0
összes=0
legn=0
kezd=input('Adj meg egy betút. ')
van=False
for i in wr:
    összes+=1
    if i[5]=='a':
        asok+=1
    if int(i[3])>int(legn):
        legn=i[3]
    if i[7]==kezd:
        van==True
print(összes,'diák van')
print(asok,'a osztályos van')
print(f'200{legn} volt az utolsó év amiben osztály indítottak.')
if van==True:
    print(f'van {kezd} kezdőbetüjű diák')
else:
    print('nincs')
wr.close