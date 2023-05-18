wr=open('ingf.txt','w')

ing=int(input('Adja meg az életévét. '))
wr.write(f'Adja meg az életévét')
if ing<40:
    print('Fiatal')
    wr.write(f'Fiatal')
elif ing>40 and ing <45:
    print('Középkorú')
    wr.write(f'Középkorú')
else:
    print('Idős')
    wr.write(f'Idős')
wr.close()