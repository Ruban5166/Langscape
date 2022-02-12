l = [10,5,8,3]
i = 0
j = 1
while j < len(l):
    i = 0
    while i < len(l)- j:
        if l[i] > l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
        i = i + 1
    j = j + 1    
    
print(l) 

# i = 0
# while i < len(l)-2:
    # if l[i] > l[i+1]:
        # l[i],l[i+1] = l[i+1],l[i]
    # i = i + 1    
        
# print(l)

# i = 0
# while i < len(l)-3:
    # if l[i] > l[i+1]:
        # l[i],l[i+1] = l[i+1],l[i]
    # i = i + 1    
    
# print(l)       