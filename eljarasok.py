

def border(n, s):
    print()
    for i in range(n):
        print('s', sep='', end='')
    print('\n')


border(80, '*')
print('1. feladat')
print('a) feladat')
border(10, '-')
print('b) feladat')
border(80, '*')
print('2. feladat')


def proc():
    global a
    a = 5
    print(b)
    c = 3
    print(c)


b = 0
c = 4
proc()
print(a)


def proc(x):
    x += 1
    print(x)


proc(3)
a = 10
proc(a)
print(a)


def pn(num):
    end = int(num/2)
    s = 1
    for i in range(2, end+1):
        if num % i == 0:
            s += i
    if s == num:
        print('tökéletes szám')
    else:
        print('Nem tökéletes szám')


for i in range(2, 1001):
    print(i, end=' ')
    pn(i)
ob = int(input('Kérem a vizsgálandó számot: '))
pn(ob)
