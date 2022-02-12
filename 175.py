discount = 20

def purTV():
    global discount
    discount = 40
    print('Opening Time -', discount)
    

def purLAPTOP():
    discount = 30
    print(discount)
    print(globals()['discount'])
    
    
    
purTV()

purLAPTOP()
    