#factorial 1,2,3,4,5

def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact (num-1)
        
result = fact(5)
print(result)            



def total(num):
    if num == 1:
        return 1
        
    else :
        return num + total(num -1)    
    
    
result = total(5) 

print(result)   