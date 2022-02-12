def totalcalculator (*n):
    total  = 0
    for sub in n:
        total = total + sub
    print(total)


totalcalculator(90,50,100)    




def calculatortotal(**keword):
    total = 0
    for sub , mark in keword.items():
        total = total + mark 
        print(sub ,'scord', mark)
    print(total)


calculatortotal(tamil = 90,maths = 100, science = 100)