# * 1 2 3 4 5
# * * 1 2 3 4
# * * * 1 2 3
# * * * * 1 2
# * * * * * 1

for col in range(5):
    for col2 in range(col+1):
         print('*',end = ' ')
    for row in range (1,6-col):
        print(row,end = ' ')
    print()