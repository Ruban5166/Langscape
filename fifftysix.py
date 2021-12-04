#fibonacci series
cont = int(input('Enter the contion:'))
firstNo = -1
secoundNo = 1


for i in range(cont+1):
    thiardNo = firstNo+secoundNo
    # secoundNo = firstNo+secoundNo
    # firstNo = secoundNo-firstNo
    firstNo = secoundNo
    secoundNo = thiardNo
    
    
    print('\n',firstNo,secoundNo,thiardNo)