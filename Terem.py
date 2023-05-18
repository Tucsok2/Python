class Terem():
    def __init__(self,islokanév,terem,padszám,ülésszám,):
        self.iskolanév=islokanév
        self.terem=terem
        self.padszám=padszám
        self.ülesszam=ülésszám
    def teremsz(self):
        if self.terem>25:
            return 'Nagy iskola'
        else:
            return 'Kis iskola'
    def letszam(self):
        ülesszam=self.padszám*2
terem=[]
for _ in range(3):
    iskolanév=input('Mi az iskola neve? ')
    terem=int(input('Mennyi a termek száma? '))
    padszám=int(input('Hány pad van?'))
    t=Terem(islokanév, terem, padszám, ülésszám)
    terem.append(t)

for t in terem:
    print(f'Az {t.iskolanév}{teremsz(t.teremsz)}{terem}{ülesszam}')