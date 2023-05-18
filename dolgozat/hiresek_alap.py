class Cipő:
    def __init__(self,ringli,anyag,méret):
        self.ringli = ringli
        self.anyag = anyag
        self.méret = méret

    def nöi(méret):
        if méret<=41 and méret>=35:
            return 'Női'
        else:
            return 'Férfi'
    def cipőfűző(ringli):
        if ringli == 2:
            return(f'Kicsi: 45,Közepes: 75,Nagy: 75')
        elif ringli == 3:
            return(f'Kicsi: 60,Közepes: 75,Nagy: 90')
        elif ringli == 4:
            return(f'Kicsi: 75,Közepes: 90,Nagy: 100')
        elif ringli == 5:
            return(f'Kicsi: 75,Közepes: 100,Nagy: 120')
        elif ringli == 6:
            return(f'Kicsi: 75,Közepes: 120,Nagy: 150')
        elif ringli == 7:
            return(f'Kicsi: 90,Közepes: 120,Nagy: 150')
        elif ringli == 8:
            return(f'Kicsi: 90,Közepes: 120,Nagy: 180')
        elif ringli == 9:
            return(f'Kicsi: 120,Közepes: 150,Nagy: 180')
        elif ringli == 10:
            return(f'Kicsi: 120,Közepes: 150,Nagy: 200')
    def fugg(meret):
        if meret == 35 and meret == 41:
            return "Női"
        else:
            return "Férfi"

    def fugg2(anyag):
        if anyag == "b":
            return "bőr"
        else:
            return "Mesterséges"