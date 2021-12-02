#common multible number finding
number1 =  int(input('Enter the Number 1st number:') ) #2
number2 = int(input('Enter the 2nd number:')) #5

if  number1 > number2:
    big = number1
elif number2 > number1:
    big = number2      #5

while True:

    if big%number1 == 0 and  big%number2 == 0: 
        print('Common multible number is',big)
        break
    big = big + 1
