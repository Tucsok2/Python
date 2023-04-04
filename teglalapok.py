def b_oldal(teglalap):
    return teglalapok[1]

teglalapok=[[1,9],[2,3],[5,7]]
print(max(teglalapok))
print(max(teglalapok, key=b_oldal))
print(max(teglalapok, key=lambda teglalap:teglalap[1]))
print(max(teglalapok, key=lambda tl:tl[0]*tl[1]))
köszönt=lambda vezetéknév, keresztnév: szia={vezetéknév}{keresztnév}
