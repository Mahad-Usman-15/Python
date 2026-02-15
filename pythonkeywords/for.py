import math
def isPrime(num):
    if num<1:False
    if num<=3:True
    sqrt=int(math.sqrt(num))
    for i in range(2,sqrt+1):
        if num%i==0:
            return False 
    
    return True

print(isPrime(10))