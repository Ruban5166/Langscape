#converting to modulas
rem = ''
reve = ''

number1 = int(input('enter the number:'))
while number1>0:
    reminder = number1%2
    rem = str(reminder)
    reve = reve + rem 
    
    print(reminder)
    number1 = number1//2

print(reve)

lenth = len(reve)
while lenth>0:
    print(reve[lenth-1],end='')
    lenth = lenth-1