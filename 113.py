#input A5B6
#output AAAAABBBBBB
code = 'A5B6C7'

lenth = len(code)
print(lenth)
decode = ''
i = 0
while i < lenth:
    decode = decode+code[i]#a
    print(decode)
    print()
    decode =decode * int(code[i+1]) #aaaaa
    print(decode)
    print()
    i = i+2
print(decode)