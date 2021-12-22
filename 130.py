l = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ]
    
su = 0   
for i in range(len(l)):
    # print('index :',i)
    # print(l[i])
    
    for j in range(len(l[i])):
        if i == j:
            print(l[i][j])
            su = su + (l[i][j])
print(su) 




for i in range(len(l)):
    # print('index :',i)
    # print(l[i])
    
    for j in range(len(l[i])):
        # if i == j:
            print(l[j][i])
            # su = su + (l[i][j])
    
# print(su           