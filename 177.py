#recurision 

def getUsernamePassword(username,password):
    if username != 'abcd':
        print('Incorect Username')
        username = input('Enter the Username : ')
        password = input('Enter the Password : ')
        getUsernamePassword(username,password)
    
    elif password != 'abcd':
        print('Incorect password')
        username = input('Enter the Username : ')
        password = input('Enter the password : ')
        getUsernamePassword(username,password)
    
 
username = input('Enter the username : ') 
password = input('Enter the password : ')
getUsernamePassword(username,password)  