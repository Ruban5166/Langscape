#5 6 7 8 9
#4 5 6 7
#3 4 5
#2 1
#1
row = 5


while row>0:
    col = 1
    while col<=row:
        print(col+row-1,end='')
        col= col+1
    print()
    row = row-1    
 
