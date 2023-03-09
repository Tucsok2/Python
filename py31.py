Mondat=None
while Mondat!='':
    Mondat=input('Adj meg egy mondatot! ')
    if Mondat[-1]=='.':
        print('kijelentő')
    elif Mondat[-1]=='!':
        print('felkiáltó / felszólító / óhatjtó')
    elif Mondat[-1]=='?':
        print('kérdő')
