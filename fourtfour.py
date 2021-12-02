#modulas to binary
import math 
i = 0
total = 0
num =int(input('Enter the number you need to convert:'))#110
while num > 0:
    reminder = num%10 #0
    multi = reminder *(int(math.pow(2,i)))
    total = total + multi
    num =num//10 #11
    i = i+1
    
    print('reminder',reminder)
    print('multi2',multi)
    print('num',num)

print('Number is:',total)