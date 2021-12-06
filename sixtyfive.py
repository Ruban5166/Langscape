row=5
while row>0:#5 4 3 2 1
    col = 1 #1
    while col<=row: #col = 2 row = 4
        print(row+col,end =' ')
        col = col+1       #5 6 7 8  
    print()               #4 5 6  
    row=row-1             #3 2 
                          #2  