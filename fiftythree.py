#reverse the name or word
word=input('Enter the name you nedd to revers:')
lenth = len(word)

for i in range(lenth-1,-1,-1):
    print(word[i],end='')
    
