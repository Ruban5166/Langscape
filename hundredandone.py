email =input('Enter your email id: ')
lenth = len(email)
i= 0
while i<lenth:
    if not (email[i]>='0'and email[i]<='9'):
        if not (email[i]>= 'a'and email[i] <='z'):
            print(email[i],end=' ')
    i=i+1  
print()    
    
    
    
email= 'sriruban5199@gmail.com'
for x in email:
    if x >= 'a' and x<='z':
        print(x,end = ' ')