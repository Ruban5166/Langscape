name = input('Enter the word you nee to count:')
lenth = len(name)
word = 1
index = 0
while (index<lenth-1):
    if name[index]==' ':
        if name[index+1]>='a'and name[index+1]<='z':
            word=word+1
    index =index+1

print('number of word:', word)
        