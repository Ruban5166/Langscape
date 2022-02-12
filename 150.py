l = [72,86,36,49,52,85]


n = len(l) - 1
for j in range (0,n):
    for i in range(0,n):
        if l[i] > l[i + 1]:
            l[i],l[i + 1] = l[ i + 1],l[i]
    
    n = n - 1                
    
    
    
print(l)    




l = [72,86,36,49,52,85]

i = 0
j = 1
while j < len(l):
    i = 0
    while i < len(l)-1:     
        if l[i] > l[i + 1]:
            l[i],l[i + 1] = l[i + 1],l[i]
        i = i + 1    
        
    j = j + 1    
        
print(l)   




s = 'COMPUTER'

n = len(s)
j = 0
for j in range(n):    
    for i in range(n):
        print(s[i],end = ' ')
    print()
    n = n- 1    
    
    