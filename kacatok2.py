kacatok=[]
kacat='bármi'
while kacat!='elfogyott':
    kacat=input('Kérek egy kacatot! ')
    if kacat!='elfogyott':
        kacatok.append(kacat)

kacatokfel=', '.join(kacatok)
print('A kacatjaim: ',kacatokfel,',',sep='')