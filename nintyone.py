name = 'lenin'
count = len(name)

for row in range(count):
    for col in range(count):
        print(name[col] ,end = ' ')
    print()
    count = count -1    
    
    
    
    
    
name = 'lenin'
count = len(name)
count2 = count

for row in range(count):
    for col in range(count2):
        print(name[col] ,end = ' ')
    print()
    count2 = count2 -1       
    
    
    
name = 'srikishantharuban'
count =len(name)

for row in range(count):
    for col2 in range(count +1):
        print(' ' , end = ' ')
    for col in range(count -row):
    
        print(name[col],end = ' ')
    print()    
                