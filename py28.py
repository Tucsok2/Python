szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
ts=[]
for szo in szavak:
    if szo[0]=='T' or szo[0]=='t':
        ts.append(szo)
print(ts)