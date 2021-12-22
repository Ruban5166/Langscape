#
name = input('Enter your name :')
rename = []
letter = ''
lenth = len(name)
while 0 < lenth:
    letter = letter + name[lenth-1]
    lenth=lenth-1
    

print(letter)
rename = letter.split()
print(rename)   