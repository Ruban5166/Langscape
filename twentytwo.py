#number of words
name =input('enter the sentance:')
lenth =len(name)
index = 0
count = 1
while   index<lenth:
    # if name[index] == 'a' or name[index]=='e' or name[index]=='i' or name[index]=='o' or name[index]=='u':
    if name[index] ==' ':
        count = count+1
       
    index =index+1
print('Number of words:',count)