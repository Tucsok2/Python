


NÉMET=19
BRIT=20
CSEH=21
LENGYEL=23
MAGYAR=27
netto_ár=float(input('hogyér\' adnak egy mütyürkét?'))
print(f'A mütyürkét brutto árai: ')
print(f'{netto_ár*(1+NÉMET/100):10.2f}picula németországban')
print(f'{netto_ár*(1+NÉMET/100)}picula ködösben')
print(f'{netto_ár*(1+NÉMET/100):5.2f}picula Svejk hazájában')
print(f'{netto_ár*(1+NÉMET/100):<10.2f}picula németországban')
print(f'{netto_ár*(1+NÉMET/100):^10.2f}picula németországban')