#reverse number
no = input('Enter the  number:')
lenth =len(no)
index =lenth-1

while index>=0:
    print(no[index],end='')
    index=index-1