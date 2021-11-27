subject = int(input('Enter the number of subjects:'))
sub2 = subject
total = 0
while 0<subject:
    marks = int(input('Enter your marks'))
    total =total+marks
    subject=subject-1
    
print(total)
print(total/sub2)    