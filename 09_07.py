#ctrl + ü egysor

'''
a=3
b=5
'''

a = int(input('kérek egy számot')) #típuskonverzió
b = int(input('kérek egy másik számot'))
c = a+b
8

a = int(input('kérek egy számot')) #típuskonverzió
b = input('kérek egy másik számot')
c = a+b
35

print(a)
print(b)
print(a+b)
print(c)

print(f'Az {a} és {b} összege {c}-vel egyenlő')

if a>b:
    print(f'a nagyobb mint b')
    print(f'{a} nagyobb mint {b}')
    
elif b>a:
    print(f'b nagyobb mint a')
    print(f'{b} nagyobb mint {a}')
else:
    print(f'A két szám egyenlő')
if a %2==0:
    print('páros')
else:
    print('páratlan')

------------------------------------------------
#1

a = int(input('Kérek egy számot'))
b = int(input('Kérek egy másik számot'))
c = int(input('Kérek egy  számot'))
print=('A háromszög kerülete',a + b + c)