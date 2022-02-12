employess = {'kathiravan':50000,'viyan':40000,'Navilan':25000,'Arul':35000}
names = []
for name,salary in employess.items():
    if salary > 25000:
        print(name,'--->',salary)
        names.append(name)
        
        
print(names)        