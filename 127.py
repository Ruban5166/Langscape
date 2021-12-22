#'sun','mon','tues',''wednes','thurs','fri','satur'

l1 = ['sun','mon','tues','wednes','thurs','fri','satur']
l2 = []
lenth = len(l1)
i = 0
string = '' 
while i < lenth:
       
     l2.append(l1[i]+'day')
     string = ' '.join(l2)
     i =i+1
 
print(l2)
print(string) 
