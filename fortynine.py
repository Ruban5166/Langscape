#addition of first 10 numbers
total = 0
value = int(input('Enter the value number:'))
for no in range(1,value+1):
    total =total+no
    print(no,end =' ')
print('\n',total)