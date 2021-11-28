#factorial
no = int(input('Enter the number:'))
total =1

while no>1:
    total = total*no
    no=no-1
print('factorial number:',total)    