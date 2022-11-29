

c = int(input('Hány fok van(celsius)? '))
k = c-(272.15)
print(k)
if c <= 18:
    print('hideg')
elif c <= 25:
    print('elviselhető')
else:
    print('hőség van-e?')
