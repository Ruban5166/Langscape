#inventory
goods = {}

total = 0
while True:
    name = input('Enter the name: ')
    price = int( input('Enter the price: '))
    total = total+price
    doYouWantCon = input('Do you want to continue :(y / n)')
    if doYouWantCon == 'n' or doYouWantCon =='N':
        break
        
        
print(total)        