
hof=float(input('Kérem adjon meg egy hőfokot '))

op=1539
fp=2750

if hof<op:
    print('Szilárd')
elif hof<fp:
    print('Folyékony')
else:
    print('Gáz')