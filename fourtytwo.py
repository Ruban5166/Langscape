#Fibonacci
firstnumber = -1
secoundnumber = 1
thrednumber = 0
count = 10


while count >0:
    print(firstnumber,' ',secoundnumber,' ' , thrednumber ,end = '\n')
    
    secoundnumber = firstnumber +secoundnumber
    firstnumber = secoundnumber- firstnumber
    thrednumber = firstnumber +secoundnumber
    
    count= count-1
    
