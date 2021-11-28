#sum of digits 4+3+2+1=10
no= input('enter the number:')
lenth =len(no)
index = lenth-1
sumOfDigts = 0
while index >=0:
    sumOfDigts = sumOfDigts+ int(no[index])
    index=index-1

print('sum of dights:',sumOfDigts)
