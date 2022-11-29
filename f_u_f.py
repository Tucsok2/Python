import random

feldsok=[]
for _ in range(10):
    feldob=random.choice(["f","í"])
    feldsok.append(feldob)
print('A feldobások:',', '.join(feldsok))

f_u_f=0
for index,feldob in enumerate(feldsok):
    if index>0 and \
        feldob=='f' and feldsok[index-1]=='f':
            f_u_f+=1

print('Ennyiszer volt fej után fej: ',f_u_f)