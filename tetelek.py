
count=0
t=[2,5,6,9,10,12,4]
'''
# print(f'Az 5-nél nagyobb számol{count}')
print("eldöntés --True/false")
wr=open('eldontes.txt','w')
wr.write('t=[2,5,6,9,10,12,4]')
n=len(t)
wr.write(f'{n}')
ker=5
wr.write('A keresett szám:{ker}')
i=0
while i<n and t[i]!=ker:
    i+=1
if i<n:
    print('Van ilyen ',ker)
    wr.write(f'Van ilyen \n')
else:
    print('Nincs ilyen ',ker)
    wr.write(f'Nincs ilyen \n')
wr.close()
'''


'''
n=len(t)
ker=5
i=0
while t[i]!=ker:
    i+=1
print('ezen a helyen található', i +1)
'''

'''
# print('eldöntés (van.nincs), kiválasztás tétel (hely megadás')
n=len(t)
print(n)
ker=5
i=0
while i<n and t[i]!=ker:
    i+=1
    if (i<n):
        print(f'van{ker} elem a listában')
        print(f'Helye{i+1}')
    else:
        print(f'nincs{ker} elem a listában')
'''


'''
wr=open('max.txt','w')
maxElem=t[0]
wr.write(f't=[2,4,7,1,8,5,9]\n')
for elem in t:
    if elem> maxElem:
        maxElem=elem
print(maxElem)
wr.write(f'{maxElem}\n')
wr.close()  

wr.open('min.txt','w')
minElem=t[0]
wr.write(f't=[2,4,7,1,8,5,9]\n')
for elem in t:
    if elem< minElem:
        minElem=elem
print(minElem)
wr.write(f'{minElem}\n')
wr.close()
# print(f'egyszerü számtani átlag:')



b=[]
c=[]
d=[]
def dupla (num):
    return num*2

for elem in t:
    b.append(dupla(elem))
    if elem%2==0:
        c.append(elem)
    if elem<5:
        d.append(elem)
    if elem%2!=0:
        e.append()
print(b)
print(c)

print('kiválogatás')
print(d)
'''
t=[2,5,6,9,10,12,4]


n=len(t)
for i in range(n-1,0,-1):
    for j in range(0,i):
        if (t[j]>t[j+1]):
            tmp=t[j+1]
            t[j+1]=t[j]
            t[j]=tmp
print[t]

