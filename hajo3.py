class Hajo:
    def __init__(self,neve,kapneve,arboc,sebesseg,orszag):
        self.neve=neve
        self.kapneve=kapneve
        self.arboc=arboc
        self.sebesseg=sebesseg
        self.orszag=orszag
    def valto(sebesség):
        return sebesség*1.852
    def arboc_m(magasság):
        return magasság/100
    def kapnev(neve):
        return neve.title()
    def nemzet(orszag):
        if orszag=='o':
            return 'orosz'
        elif orszag=='a':
            return 'amerikai'
Hajo=[]
for _ in range(3):
    neve=input('Adja meg a hajó nevét! ')
    h=int(input('Árbóc magassága! '))
    kapneve=input('kapitány neve! ')
    seb=int(input('Adja meg a hajó sebességét! '))
    orszaga=input('Adja meg a hajó országát (a/o)! ')
    sello=Hajo(neve,kapneve,h,seb,orszaga)
