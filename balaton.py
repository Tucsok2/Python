class Balaton():
    def __init__(self, település, fekvés, szám):
        self.település = település
        self.fekvés = fekvés
        self.szám = szám
    def fugg(self):
        if self.fekvés == "é":
            return 'északi'
        else:
            return 'déli'
    def elotag(self):
        if self.szám <= 5000:
            return 'falu'
        elif self.szám >= 5000 and self.szám <= 10000:
            return 'nagyközség'
        else:
            return 'város'

telepulesek = []
for _ in range(1):
    település = input("Add meg egy település nevét! ")
    fekvés = input("Add meg a fekvését (é/d)! ")
    szám = int(input("Add meg a lakosság számát! "))
    telepulesek.append(Balaton(település, fekvés, szám))
for telepules in telepulesek:
    print(f"{telepules.település} egy {telepules.fugg()} parti {telepules.elotag()}, {szám} fővel.")