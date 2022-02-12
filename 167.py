def odd_even(no):
    if no%2 == 0:
        print('even')
    else:
        print('odd')
        
        
num = int(input('Enter the number : ')) 
odd_even(num)


for num in range(1,5):
    odd_even(num)