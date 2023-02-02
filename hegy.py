hegy1=input('Add meg egy hegy magaságát! ')
hegy2=input('Add meg egy másik hegy magaságát! ')
if hegy1>hegy2:
    print('Az első hegy nagyobb.')
elif hegy2>hegy1:
    print('A második hegy nagyobb.')
else:
    print('A két hegy egyenlő magas')

nev=None
for _ in range(3):
    nev=input('Adja meg a mászó nevét! ')
