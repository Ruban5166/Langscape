name =input('enter your name:')
lenth =len(name)
index = 0
count = 0
while   index<lenth:
    # if name[index] == 'a' or name[index]=='e' or name[index]=='i' or name[index]=='o' or name[index]=='u':
    if name[index] in['a','e','i','o','u']:
        count = count+1
        print(name[index])
    index =index+1
print('number of vowels are:',count)