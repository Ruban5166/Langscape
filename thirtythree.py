#prime no
no = int(input('Enter the number:'))
count = 2
while count<no:
        if no%count==0:
            print('NOT PRIME NUMBER')
            break
        count = count+1
else:
    print('PRIME NUMBER')
    