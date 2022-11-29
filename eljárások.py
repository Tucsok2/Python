'''

def alahuzas():
    for _ in range(10):
        print('.',end='')
    print()

print('ez egy fontos figyelmeztetés')
alahuzas()
print('minden sora nagyon fontos!')
alahuzas()
print('komolyan')
alahuzas()
'''


def pluszkettő(szám):
    print(szám+2)

print ( '5+2= ',end='')
pluszkettő(5)

def pluszkettő(szám):
    return(szám+2)
print ( '5+2= ',pluszkettő(5))
