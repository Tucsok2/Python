import random

a=int(5)
b=int(random.randint(5,25))
c=int(input("Adj meg egy számot"))

print("Öszzegük: ",a+b+c)
szorzat=a*b*c
print("Szorzatuk: ",szorzat)

if szorzat>500:
    print("A szorzatuk nagyyobb mint 500")
elif szorzat<500:
    print("A szorzatuk kisebb mint 500")
else:
    print("A szorzatuk 500")


