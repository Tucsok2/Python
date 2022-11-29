
aug1=False
aug= [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]

if len(aug)==31:
    aug1=True
    print(f'ez augusztus adatsora')
else:
    print(f'ez nem augusztus adatsora')

legnagyobb=aug[0]
for num in aug:
    if num>legnagyobb:
        legnagyobb=num
print(legnagyobb)

legkisseb=aug[0]
for num in aug:
    if num<legkisseb:
        legkisseb=num
print(legkisseb)

felett=0
for num in aug:
    if num>31:
        felett+=1
print(felett)


ker=20
print(aug[ker+1])

össz=0
for num in aug:
    össz=num+össz

átlag=össz/len(aug)

hőin=legnagyobb-legkisseb
print(hőin)



wr=open('aug.txt','w')
wr.write(f'legnagyobb hőmérséklet: {legnagyobb}\n')
wr.write(f'legalacsonyabb hőmérséklet: {legkisseb}\n')
wr.write(f'{felett} alkalommal volt 31 fölött \n')
wr.write(f'20-án mennyi volt:{aug[ker+1]}\n')
wr.write(f'átlag: {átlag}\n')
wr.write(f'hőingadoszás: {hőin}\n')
wr.close()