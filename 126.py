# WISH YOU A VERY HAPPY NEW YEAR


sen ='WISH YOU A VERY HAPPY NEW YEAR'
l1 = sen.split()
l2 = []
lenth =len(l1)
i = 0
while i<lenth :
    if i%2 == 0 :
        l2.append(l1[i][::-1])
    else:
        l2.append(l1[i])    
    i = i+1
print(l2)   
    