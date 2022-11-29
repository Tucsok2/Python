import math, cmath

a=float(input("másodfokú tag együthatója"))

while a==0:
    print("Ebböl nem lesz másodfokú.")
    a=float(input("Kérek egy számot"))


b=float(input("elsőfokú tag együthatóját"))
c=float(input("konstans"))

d=b*b+4*a*c
