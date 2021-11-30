no = input('Enter the number:')
lenth = len(no)
index = lenth-1
reverse = ''

while index>=0:
    print(no[index])
    reverse = reverse+ no[index]
    index= index -1
print(reverse)

if reverse==no:
    print(' Palidrame')
else:
    print('not Palidrame')
    