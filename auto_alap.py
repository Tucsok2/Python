class Híres_auto:
    def __init__(self, márka_név, henger_térfogat, nemzetiség):
        self.név = márka_név
        self.henger_térfogat = henger_térfogat
        self.nemzetiség = nemzetiség

    def elotag(self):
        if self.nemzetiség == 'n':
            return 'német'
        else:
            return 'japán'


