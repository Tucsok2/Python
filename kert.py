
barack_m=int(input("Hány mázsa barack termet " ))
barack_á=int(input("Menyibe kerül a barackot (Ft/kg) "))
körte_m=int(input("Hány mázsa körte termet "))
körte_á=int(input("Menyibe kerül a körtét (Ft/kg) "))

barack_ö=barack_m*barack_á*100
körte_ö=körte_m*körte_á*100
print(barack_ö)
print(körte_ö)

if barack_m>körte_m:
    print("barack több")
elif körte_m>barack_m:
    print("körte több")
else:
    print("egyenlő")

if barack_á>körte_á:
    print("barack drágább")
elif körte_á>barack_á:
    print("körte drágább")
else:
    print("egyenlő")

if barack_ö>körte_ö:
    print("barack több a bevétel")
elif körte_ö>barack_ö:
    print("körte több a bevétel")
else:
    print("egyenlő")