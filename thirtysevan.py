no = int(input('enter the number :'))
number1 = 0
number2 = 0
revese = 0
while no>0:
    revese = (revese*10) + (no%10)
    number2 = no//10
    
print(revese)

