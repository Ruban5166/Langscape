#comparing list objects

a = ['ruban','sri','kishantha','farazad','isanul','hugi']
b = ['ruban','sri','kishantha','farazad','isanul','hugi']

# print(a==b)

# print(a is b)

l = [[5,10,15,20],[25,30,35],[40,45,50]]

l1 = [5,10,15,20,25,30,35,40,45,50]

for x in l1:
    print(x,end = ' ')
    
for x in l:
    print(x)
        
    
    
for x in range(len(l)):
    print(l[x])