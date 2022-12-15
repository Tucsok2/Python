kedd=int(input('Hány forintot kölöttél kedden? '))
szerda=int(input('Hány forintot kölöttél szerdán? '))

if kedd>szerda:
    print(f'Kedden költöttél többet,{kedd}')
elif szerda>kedd:
    print(f'Szerdán költöttél többet,{szerda}')
else:
    print(f'Kedden és szerdán is ügyanannyit költöttél,{szerda,kedd}')
