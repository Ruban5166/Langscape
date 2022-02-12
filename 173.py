def calculator(no1,no2):
    add = no1 + no2
    sub = no1 - no2
    mul = no1 * no2
    div = no1 // no2
    return add, sub, mul, div
resulat = calculator(100,50)  

for x in resulat:
    print(x)
    
    
    
        
    
def greetings(name,msg):    
    print('Hi',name,msg)
    
 
 
greetings(msg = 'Well come to python world',name = 'Ruban')




def defa(name,msg = 'Good Morning'):
    print('Hi',name,msg)
    
    
defa('Srikishantharuban')    
    