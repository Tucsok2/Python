cipo1=int(input('Adj meg az egyik cipő méretet!'))
cipo2=int(input('Adjon meg egy másik cipő méretet!'))
if cipo1>cipo2:
    print('A cipő méret az egyik cipő esetében nagyobb,')
elif cipo1<cipo2:
    print('A cipő méret a másik cipő esetében nagyobb')
else:
    print('A két cipő mérete egyenlő')