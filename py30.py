Mondat=input('Adj meg egyy mondatot! ')

if Mondat[-1]=='.':
    print('kijelentő')
elif Mondat[-1]=='!':
    print('felkiáltó / felszólító / óhatjtó')
elif Mondat[-1]=='?':
    print('kérdő')
