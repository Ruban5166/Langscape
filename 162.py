# forloop using for bubble sorting

l = [10,5,8,3]

n = len(l)-1
for j in range(0,n):
    for i in range(0,n):
        if l[i] > l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]  
    n = n - 1 
    
    
print(l)    



l = [10,5,8,3]

print(sorted(l))