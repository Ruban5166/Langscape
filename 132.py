name = ['ruban','usan','selin','raja','gower',]
time = [9.5,10.8,9.8,11.1,10.1,]
record = []

for x in range(len(name)):
    for y in range(len(time)):
        if x==y:
            record.append([name[x],time[y]])
    print()        
    
    
    
print(record)    

#[['ruban', 9.5], ['usan', 10.8], ['selin', 9.8], ['raja', 11.1], ['gower', 10.1]]
# record[0][0:1]  record[1][0:1]  record[2][0:1]  record[3][0:1]  record[4][0:1]  
lenth = len(record)
i = 0
x = len(record)
while i < lenth + 1:
    if x ==0:
        break
        if record[i][i:x]>record[i+x][i+x:x]:
            record[i][i:x] = record[i+x][i+x:x]
        else :
        
            record[i][i:1]=record[i][i:1]
        
        i = i +1
    x = x -1
 

print(record)        
        