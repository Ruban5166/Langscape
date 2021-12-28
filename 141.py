#geting marks from students

register ={}

no = int(input('Enter the number of student: '))

i = 1
while i <= no:
    name =  input('Enter the name: ')
    marks = int(input('Enter the marks: '))
    register[name] = marks
    i = i + 1
    
    
print(register)    