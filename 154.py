#Geting inputs from user

register = {}

# no = int(input('How many students you need to enter :'))

# i = 1

while True:
    name = input('Enterthe name: ')
    marks = input('Enter marks: ')
    register[name] = marks
    # i = i + 1
    nextCanditae = input('Do you want to continue:(y/n)')
    if nextCanditae == 'n' or 'N':
        break
    
print(register)