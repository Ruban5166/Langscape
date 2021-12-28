#croseary shop list making

register ={}
total = 0
while True:
    name  = input('Enter the name: ')
    price = int(input('Enter the price: '))
    register[name] = price
    total = total + price
    nextContinue = input('Do you want to continue ( y/n ): ' )
    
    if nextContinue == 'n':
        break
        
        
print(register)

print(total) 
print(total)