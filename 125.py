#input = 'WISH YOU A VERY HAPPY NEW YEAR'

sentance = 'WISH YOU A HAPPY NEW YEAR'
l1 = sentance.split()
l2 =[]

lenth = len(l1)
while 0 < lenth :
    l2.append(l1[lenth-1])
    lenth = lenth - 1
    
print(l2)