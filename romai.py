tallies = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

def RomanNumeral1ToDecimal(romanNumeral1):
    sum=0
    for i in range(len(romanNumeral1)-1):
        left=romanNumeral1[i]
        right=romanNumeral1[i+1]
        if tallies[left]<tallies[right]:
            sum-=tallies[left]
        else:
            sum+=tallies[left]
    sum+=tallies[romanNumeral1[-1]]
    return sum

roman=input('Enter Roman Numbers: ')
RomanNumeral1ToDecimal(roman)
print(RomanNumeral1ToDecimal(roman))