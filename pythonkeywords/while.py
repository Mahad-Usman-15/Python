# in	To check if a value is present in a list, tuple, etc.
# break	To break out of a loop
# continue	To continue to the next iteration of a loop
import math
# Capture the Range: Take two inputs from the user, start and end.
start = int(input("Enter the starting of the series:"))
end = int(input("Enter the ending of the series:"))
if start>end :
    end=start

p=0
# The Outer Loop (The Range): Iterate through every number $n$ from start to end.
for i in range(start,end+1):
    if i<=1:
        continue
    sqrt=int(math.sqrt(i))
    # check divisors from 2 up to the square root of $n$ ($\sqrt{n}$). If no number in this sub-range divides $n$ evenly, then $n$ is prime.
    for j in range(2,sqrt+1):
        if (i%j)==0:
            break
    else:    
     print(i)       
   
   
   

           
   
            
            
        
    
    
   

        
        

