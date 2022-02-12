price = {'Appple':100,'Orange':80,'Mango':120,'Banana':50}

for productname,productprice in price.items():
    print(productname,'-->',productprice)
    
    
price = {'Appple':100,'Orange':80,'Mango':120,'Banana':50}

for productname,productprice in price.items():
    (price[productname]) = (price[productname]) - (10/100 *price[productname])
print(price)
    
    
    
    
prices = {'Appple':100,'Orange':80,'Mango':120,'Banana':50}
l = prices.keys()
print(l)
for x in l:
    if x == 'Mango':
        del prices[x]
        break
        
print(prices)        