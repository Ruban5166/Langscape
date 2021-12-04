#no of words counts in sentance
sentance = input('Enterthe setance:')
total = 1
for words in sentance:
    if words== ' ':
        total=total+1
    print(words,end = ' ')
else:
    print('number words are:',total)