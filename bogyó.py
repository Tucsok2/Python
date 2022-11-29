név= input('Mi az ős neve? ')
bogyók=int(input('Hány Bogyója van? '))
if bogyók<10:
    minősités="zsenge"
elif bogyók>20:
    minősités="nagy koponya"
else:
    minősités='gyűjtögető'

print(f'{név} egy {minősités}.')
