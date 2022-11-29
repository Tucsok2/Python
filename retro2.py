
név=input("Mi a gép neve? ")
müköd=True if input("Működik(i/n)? ")=='i' else False
ár= int(input("Mi az ára"))

if (név=="ZX Spectrum" or név=="c64")and müköd and ár<=25000:
    print("Biznisz!!!")
else:
    print('Gagyi, 8-bitesek... Kinek kellenek?!')