import random

def alahuzas():
    print('-------------')

szam1=int(input('Írjon be egy szamot: '))
alahuzas()
szam2=random.randint(10,50)
szam3=12
print(szam1)
alahuzas()

if szam2%2!=1:
    szam2=random.randint(10,50)
print(szam2)
alahuzas()

print(szam3)
alahuzas()

if szam1%2==0:
    print('páros')
    alahuzas()
else:
    print('páratlan')
    alahuzas()

szamok=[szam1,szam2,szam3]
szamok_mas=szamok.copy()
print(szamok)
alahuzas()

szamok.append(random.randint(1,50))
print('append: ',szamok)
alahuzas()

szamok.sort()
print('sort: ',szamok)
alahuzas()

szamok.reverse()
print('reverse: ',szamok)
alahuzas()

szamok.remove(szam1)
print('remove: ',szamok)
alahuzas()

szamok.clear()
print(szamok)
alahuzas()

wr=open('egy.txt','w')
wr.write(f'{szamok_mas[0]}\n')
wr.write(f'{szamok_mas[1]}\n')
wr.write(f'{szamok_mas[2]}\n')
wr.close()

wr=open('egy.txt','r')
print(wr.readline())
print(wr.readline())
print(wr.readline())
wr.close()
