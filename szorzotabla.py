szam1=1
while int(szam1)<=10:
    szam2=1         
    while int(szam2)<=10:
        print(szam1,"*",szam2,"=",szam1*szam2)
        szam2+=1
    if szam2==10:
            szam2=1
    szam1+=1

#2
szorzandó=1
while szorzandó<=10:
    szorzó=1
    while szorzó<=10:
        print(szorzandó,'*',szorzó,'=',szorzandó*szorzó)
        szorzó+=1
    print('')
    szorzandó+=1