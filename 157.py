#----inter changing keys and values----#

employess = {'kathiravan':100,'viyan':101,'Navilan':102,'Arul':103}
employees1 = {}

for name,ids in employess.items():
    employees1[ids] = name
    
print(employees1) 



employess = {'kathiravan':100,'viyan':101,'Navilan':102,'Arul':103}

employess ={no:name for name,no in employess.items()}
print(employess)

   