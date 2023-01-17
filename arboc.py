def arboc(magasság):
    return magasság/100
def kapnev(neve):
    return neve.title()
h=int(input('Árbóc magasság! '))
neve=input('Kapitány neve: ')
print(arboc(h))
print(kapnev(neve))
