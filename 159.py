#landscape class 20
employee = {'Kathiravan':100,'Vijan':101,'Navilan':102,'Arul':103}

employee = {key:value for value,key in employee.items()}

print(employee)




employee = {'Kathiravan':100,'Vijan':101,'Navilan':102,'Arul':103}

employee2 = {}

for name,no in employee.items():
    employee2[no] = name
print(employee2) 

val =[i for i in range(5)]

print(val)   