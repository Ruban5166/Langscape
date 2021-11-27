# 2 5 10 20 25 50 100

no = 100
i = 2
while i<=no:
    if no%i == 0:
        print(i)
    i=i+1



no = 75
i = 2
while i<=no:
    if no%i == 0:
        print(i)
    i=i+1
    
    
number1 = int(input('enter the number1:'))
number2 = int(input('enter thr number2:'))
if number1<number2:
    small = number1
elif number2<number1:
        small = number2
    
i = 2
while small>=i:
    if number1%i == 0 and number2%i== 0:
        print(i)
    i=i+1