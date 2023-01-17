
def valto(sebesség):
    return sebesség*1.852



hajo1=int(input('Adja meg a hajó sebességét'))
hajo2=int(input('Adja meg a hajó sebességét'))
if hajo1>hajo2:
    print('Hajó egy gyorsabb mint hajó kettő')
elif hajo1<hajo2:
    print('Hajó kettő gyorsabb mint hajó egy')
else:
    print('Egyenlő sebességűek')

