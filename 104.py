#all letters in capitilal
name = input('enter the name: ')
for letters in name:
    if not (letters >='A' and letters <='Z'):
        print('please reenter the name in capital letters')
        break
else:
    print('Continue to secound page')            
        
print(' '.isspace())