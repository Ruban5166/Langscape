sen = 'python is very very esy to learn'
count = 0
position = 0
for i in sen:
    if i == 'y':
        count = count +1
        print(i, 'present at',position)
    position =position+1    
else:
    print('y is present in number :',count)
    
    
if count == 0:
    print('y is not present in sentance ')