
nev= input("Kére, adja meg a nevét ")
print(nev)
ÉV=int(2022)
udv=(f'Üdvőzőllek {nev}')
print (udv,'szép napot kívánok neked', sep=" ")
eletkor=int(input("kérem adja meg a születési évét"))
eletk= int(ÉV)-eletkor
if int(eletk)>=18:
    print('felnött')
elif int(eletk)<18 & eletk>14:
    print('középiskola')
else:
    print('általános')
