import cmath
import imp


import math, cmath
a= input('Kérem a másodfokú egylet fügvényhatóját: ')
a=float(a)
while a==0:
    print("ez nem lesz másodfokú egyenlet; nem oldom meg. ")
    a= input('Kérem a másodfokú egylet fügvényhatóját: ')
    a=float(a)

b=input("Kérem az elsőfokú tag együtthatóját: ")
c=input("Kérem a konstans tagot: ")
b=float(b)
c=float(c)

d=b*b-4*a*c
print("A diszkrimináns értéke",d)
''''''
if d>=0:
    print('Van valós megoldás.')
    x1=(-b-math.sqrt(d))/(2*a)
    x2=(-b+math.sqrt(d))/(2*a)
    print('Az egyik megoldás', x1)
    print('Az másik megoldás', x2)


