s1 = input('enter the name one: ')
s2 = input('enter the name two: ')

if (len(s1)<len(s2)):
    small = s1
    larger = s2
elif (len(s2)) <(len(s1)):
    small = s2
    larger =s1

    
combo = ''  
i = 0
for merch in small:
    combo = combo + s1[i]+s2[i]   
    i = i + 1

print(combo + larger[i:])