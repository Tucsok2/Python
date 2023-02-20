import random
gep=random.randint(1,3)
felh=None

while felh!=gep:
    felh=int(input('Melyik számra gondoltam? (1,3)'))
    if felh<gep:
        print('ennél többre gondoltam')
    elif felh>gep:
        print('ennél kevesebbre gondoltam')
print('egyenlő')