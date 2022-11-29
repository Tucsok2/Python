import math
import random

pi=22/7 
# magas=float(input("A henger magasága"))
# sugár=float(input("A henger sugara"))

magas=random.randint(2,10)
sugár=random.randint(2,10)



térfog=pi*magas*sugár**2
felszin=(2*(sugár**2*pi))+((2*sugár*pi)*magas)
print("A térfogat: ", térfog)
print("A felszin: ", felszin)