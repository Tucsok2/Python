ora=int(input('Hány óra van? '))
if ora>6 and ora<16:
    print('A bolt nyitva van.')
    mégido=16-ora
    print(f'Ennnyi órád van még ma boltba menni {mégido}')
else:
    print('A bolt zárva van. ')
