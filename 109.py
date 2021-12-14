#input A5B6C7
#output ABC567
s1 = 'A5B6C7'
count = ''
num = ''
for letter in s1:
    if letter.isalpha():
        count = count+letter
    elif letter.isnumeric():
        num = num +letter
print(count +num)        