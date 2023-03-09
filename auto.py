from auto_alap import Híres_auto

híres_autok = []
for _ in range(3):
    márka_név = input('Add meg a márka nevét. ')
    henger_térfogat = int(input('Add meg a henger térfogatát. '))
    nemzetiség = input('Add meg a márkát gyártó nemzetiségét. ')
    hires_auto = Híres_auto(márka_név, henger_térfogat, nemzetiség)
    híres_autok.append(hires_auto)

for hires_auto in híres_autok:
    print(f' A {hires_auto.név}, "egy híres" , {hires_auto.get_nemzetiseg()}, "márka", {hires_auto.henger_terfogat}')
