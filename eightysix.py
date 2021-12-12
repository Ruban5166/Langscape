* * * * * 1
* * * * 1   2
* * * 1   2   3
* * 1   2   3   4
* 1   2   3   4   5
col = 1
while col <=5:
    row = 1
    num = 5
    while num>=col:
        print('*' ,end =' ')
        num = num - 1
    while row<=col:
        print(row,' ', end =' ')
        row= row+1
    print()
    col = col+1    