from operator import ne


nev= input("Kérem, adja meg az autó nevét ")
márka= input("márkáját ")
orszag= input("hol készül a(z) "+ nev+" ")
végseb= int(input("végsebeségét "))
mondat1=orszag + " vidékein készül a " + nev+' '+ márka+" ami "+str(végseb)+"km/h-val megy"
print(mondat1)
mondat2="{} vidéken készül a {} {} ami {} km/h végsebességre képes.".format(orszag, nev, márka, végseb)
print(mondat2)
mondat3="{0} vidéken készül a {1} {2} ami {3} km/h végsebességre képes.".format(orszag,végseb, nev,márka, )
print(mondat3)
mondat4="{o} vidéken készül a {a} {m} ami {v} km/h végsebességre képes.".format(o=orszag,v=végseb, a=nev,m=márka, )
print(mondat4)
print(f'{orszag=}, {nev=}, {végseb=}')