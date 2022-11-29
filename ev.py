
ev1=False
ev= [2984,2348,2069,2204,2418,2037,2092,2495,2487,2827,2305,2650]

if len(ev)==12:
    ev1=True
    print(f'ez egy év adatsora')
else:
    print(f'ez nem egy év adatsora')

legnagyobb=ev[0]
for num in ev:
    if num>legnagyobb:
        legnagyobb=num
print(legnagyobb)

legkisseb=ev[0]
for num in ev:
    if num<legkisseb:
        legkisseb=num
print(legkisseb)

össz=0
for num in ev:
    össz=össz+num
print(össz)

alatt=0
for num in ev:
    if num<2400:
        alatt+=1
print(alatt)

legnhely=0
hossz=len(ev)
ker=legnagyobb
while ev[legnhely]!=ker:
    legnhely+=1
print(f'legnagyobb hely: {legnhely+1}')

legkhely=0
ker=legkisseb
while ev[legkhely]!=ker:
    legnhely+=1
print(f'legnagyobb hely: {legkhely+1}')

wr=open('evt.txt','w')
wr.write(f'a hónap amiben legtöbb született: {legnhely}\n')
wr.write(f'hányan szülletek : {legnagyobb}\n')
wr.write(f'a hónap amiben legkevesebb született: {legkhely}\n')
wr.write(f'hányan szülletek: {legkisseb}\n')
wr.write(f'összesen mennyi: {össz}\n')
wr.write(f'2400 alatt: {alatt}\n')
wr.close()