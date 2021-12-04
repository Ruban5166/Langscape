#while nested loop
#12345

row = 1
while row<=5:
    print(row,':')
    col = 1
    while col<=5:
        print((col+row),end=' ')
        col=col+1 
    print()    
    row=row+1
    
