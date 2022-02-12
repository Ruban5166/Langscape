employee = {'Kathiravan':35000,'Vijan':30000,'Navilan':25000,'Arul':20000}

for name,salary in employee.items():
    if salary > 25000:
        print(name ,' : ',salary)
        
employee = {'Kathiravan':35000,'Vijan':30000,'Navilan':25000,'Arul':20000}

salarylist =[]

for name, salary in employee.items():
    salarylist.append(name)
    
print(salarylist)    



for name in sorted(employee.values()):
    print(name)
    