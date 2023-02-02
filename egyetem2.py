class HíresEgyetem:
    def __init__(self,név,város,nemzetiség):
        self.név=név
        self.város=város
        self.nemzetiség=nemzetiség
    def elotag(self):
        if self.nemzetiség=='a':
            return 'University'
        else:
            return 'Universität'

egyetemek=[]
for _ in range(3):
    név = input('Add meg egy egyetem nevét! ')
    város = input('Add meg a az egyetem városát! ')
    nemzetiség = input('Add meg a nemzetiségét (a/n)!')
    egyetem=HíresEgyetem(név,város,nemzetiség)
    egyetemek.append(egyetem)
for egyetem in egyetemek:
    print(egyetemek.elotag(),egyetemek.név(),egyetemek.város())
    