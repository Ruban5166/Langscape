#          5
#        4   4
#      3   3   3
#    2   2   2   2
#  1   1   1   1   1


row = 5

while row>=1:
    col = 5
    num =1
    while num<=row:
        print(' ',end=' ')
        num = num+1
    while col>=row:
        
        print(row,' ' ,end=' ')
        print(row,' ' ,end=' ')
        col=col -1
    print()    
    row =row-1