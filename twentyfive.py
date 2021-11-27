emailId = input('Enter your emailid:')
lenth = len(emailId)
index = 0

while index< lenth:
    if not (emailId[index]>='0' and emailId[index]<='9'):
        print(emailId[index],end=' ')
    index=index+1