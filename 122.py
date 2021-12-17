list1= ['a','b','c','d']
list2 = []
lenth = len(list1)

while 0< lenth:
    list2.append(list1[lenth-1])
    print((list1[lenth-1]))
    lenth = lenth -1
    
print(list2)    