list1 = [10,20,30,40,50,10,20,30,40,]
count =0
for x in list1:
    if x == 20:
        count+=1
        
        
print(count)           


print(list1.count(50) )
print(list1.index(30))


list1.append(500)
print(list1)