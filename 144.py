#product with price

price =  {'Apple': 100, 'Grapes': 200, 'banana': 50, 'Orage':150}
print(price)
for productName,productPrice in price.items():
    #print(productName, '--->',productPrice)
    
    price[productName]  = price[productName] - (price[productName]*0.1)
    
print(price)    
    