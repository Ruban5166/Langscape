# nested for loop
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
for row in range(1,6):
    for col in range(1,6):
        print(col,end =' ')
    print()    
    
    
    
for row in range(1,6):
        for col in range(1,row+1):
            print(col,end = ' ')
        print()
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5        


for row in range(1,6):
    for col in range(1,row+1):
        print(row,end =' ')
    print()    
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5    


for row in range(1,6):
    for col in range(1,row+1):
        print(row +col,end =' ')
    print()
    
# 2
# 3 4
# 4 5 6
# 5 6 7 8
# 6 7 8 9 10



for row in range(1,6):
    for col in range(0,row):
        print(row+col ,end =' ')
    print()    
    
print()    
# 1
# 2 3
# 3 4 5
# 4 5 6 7
# 5 6 7 8 9
    
    
    
for row in range(1,6):
    for col in range(1,row):
        print('*',end = ' ')
    for col in range(6,row,-1):
        print(chr(col +96),end = ' ')    
    print()    
    