#prime number
number = int(input('Enter the number:'))
if number== 2:
    print('PRIME')
else:    
    
    for i in range(2,number):#2
        if number%i==0:
            print('Not prime')
            break
    else:
        print('PRIME NUMBER')

       # print(i)