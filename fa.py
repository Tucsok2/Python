import random

fa=[]
for i in range(31):
    fa.append(random.randint(50,100))
print(fa)

max=0
for num in fa:
    if num>max:
        max=num
print('a legtöbb',max)

min=100
for num in fa:
    if num<min:
        min=num
print('a legkevesebb',min)

fel82=0
for num in fa:
    if num>82:
        fel82+=1
print('82 felett',fel82)

ker=20
print(ker,'-án mennyi',fa[ker+1])

össz=0
for num in fa:
    össz=össz+num

print(össz/31)

wr=open('fa.txt','w')
wr.write(f'a legtöbb: {max}\n')
wr.write(f'a legkevesebb: {min}\n')
wr.write(f'82 felett: {fel82}\n')
wr.write(f'20-án mennyi: {fa[ker+1]}\n')
wr.write(f'átlag: {össz/31}\n')
wr.close()