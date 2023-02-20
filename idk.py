def fhely(tengerszint):
    if tengerszint<=200:
        return 'síkság vagy alföld.'
    elif tengerszint<=500 and tengerszint>200:
        return 'dombság'
    elif tengerszint>500 and tengerszint<=1500:
        return 'középhegység'
    else:
        return 'magashegység'

hely=None
while hely!='':
    hely=input('Add meg a földrajzi hely nevét! ')
    if hely =='':
        break
    tengerszint=int(input('Add meg a tengerszint feletti magasságát! '))
    print(hely,'egy',fhely(tengerszint))

    



