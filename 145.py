price =  {'Apple': 100, 'Grapes': 200, 'banana': 50, 'Orage':150}

list1 = price.keys()
print(list1)
for x in list1:
    if x =='Grapes':
        del price[x]
        break
        
print(price)        