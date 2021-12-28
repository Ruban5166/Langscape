#geting register record to dictionary

register = {}

while True:
    name = input('Enter the name: ')
    marks = int (input('Enter the marks: '))
    
    nextCandidate = input('Don want continue (y to continue n to no need to continue):')
    if nextCandidate == 'n':
        break