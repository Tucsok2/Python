import random

#1
szám=0
while szám<10:
    szám+=1
    print(szám)
print('')

#2
szám2=10
while szám2>0:
    print(szám2)
    szám2=szám2-1

#3
szám3=10
while szám3>0:
    if szám3%2==0:
        print(szám3)
    szám3-=1

#4

megadott_jelszó=input('Adje meg a jelszót ')
szöveg=input('')
jelszó=input('Mi a jelszó ')
while jelszó!= megadott_jelszó:
    jelszó=input('Mi a jelszó')
print(szöveg)


#5

páratlan = True
szám5 = int(input('Adj meg egy számot? (1-10)'))
while páratlan:
    print('Nem jó')
    szám5 = int(input('Adj meg egy számot? (1-10)'))
    if szám5%2==0:
        folytatja = False
print('>> Program vége! <<')


#6



hármas=0
for i in range(20):
    szám6=random.randint(1,12)
    if szám6%3==0:
        print(szám6)
        hármas+=1
print('összes hármas',hármas)
    
