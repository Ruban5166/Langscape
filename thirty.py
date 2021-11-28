#least common multible(LCM).of given number.

no1 = int(input('Enter the number1:'))
no2 = int(input('Enter the number2:'))
if  no2>no1:
    big = no2
elif no1>no2:
    big = no1

while True:    
    
    
    if big%no2==0 and big%no1==0:
        print('least comman multble numbe:',big)
        break
    big=big+1