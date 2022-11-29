import random

szamlalo=0
hatos=0
while szamlalo<=1000000:
    dobás=random.randint(1,6)
    if dobás==6:
        hatos+=1
    szamlalo+=1
print(hatos)
