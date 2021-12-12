sen = 'python is very very easy to learn'
position =-1
lenth=(len(sen))
count = 0
sticker = False
while True:
    position = sen.find('b',position+1,lenth)
    
        
    if position == -1:
        break
    count = count+1    
    print('y is present at:',position)
    sticker = True
print(count)
print('b is not present at all')