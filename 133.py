# list comprehension

ll = []
for i in range(1,6):
    ll.append(i**i)
print(ll) 

print()



ll = [i**i for i in range(1,6)] 

print(ll)  
    
    
ll2 = []
for x in ll:
    if x%2==0:
        ll2.append(x)
        
print(ll2)        


ll2 = [x for x in ll if x%2==0]
print(ll2)




names = ['celin','stepan','rajarajn','vidiya']

name = [names[0] for name in names]
print(name)