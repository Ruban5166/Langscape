l1 = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ]
l2 = l1[:]  
print('Bfore transporting matrix')   
for i in range(len(l1)):
    ll = l1[i]
    for j in range(len(l1[i])):
        print(l1[i][j],end = ' ')
    print( )   


for i in range(len(l1)):
    ll = l1[i]
    for j in range(len(l1[i])):
        print(l1[j][i],end = ' ')
    print( )      
        
    
print('After transporting matrix') 
for i in range(len(l1)):
 
    for j in range(len(l2)):
        l1[i][j] = l2[j][i]
        print(l1[i][j])
        
# for i in range(len(l1)):
    # ll = l1[i]
    # for j in range(len(ll)):
        # print(l1[i][j],end = ' ')
    # print( )     