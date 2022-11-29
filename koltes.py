ked=int(input('Hány forintot költöttél kedden? '))
szerda=int(input('Hány forintot költöttél szerdán? '))
if ked>szerda:
    print("Kedden költöttél többet,",ked,"Ft-ot")
elif ked<szerda:
    print("Szerdán költöttél többet,",szerda,"Ft-ot")
else:
    print("Kedden és szerdám ugyanannyit költöttél")
