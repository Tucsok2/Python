# Írjon programot tengerszint néven!
# Kérjen be addig földrajzi hely nevét és tengerszint feletti magasságát, 
# amíg üres karaktert nem üt a felhasználó!

# Írjon függvényt!
# a tengerszintek néven, amely alföldet,"dombságot,"középhegység" és "magashegység" különböztet meg!
# 200m alatt alföldet,
# 200m és 500m között dombságot
# 500m és 1500m között középhegység
# 1500m magashegység


# # Fájl írása tenger.txt néven az amelyben az összes eredmény szerepel!

# Beadandó

# A program forráskódja .py kiterjesztéssel a Githubra!
# A program forráskódja .txt kiterjesztéssel dkt-ra!
def tengerszintek():
    if tengerszint<200:
        print('alföld')
    elif tengerszint<500:
        print('dombság')
    elif tengerszint<1500:
        print('középhegység')
    else:
        print('magashegység')


hely=None
tengerszint=None
while hely or tengerszint!='':
    hely=input('földrajzi hely neve: ')
    if hely=='':
        break
    tengerszint=int(input('tengerszint feletti magasság: '))
    if tengerszint=='':
        break
    tengerszintek()
    

