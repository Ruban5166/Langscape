no = int(input('enter the number you need to reverse:'))
no2 =no
sumOfrevers = 0
count = 0
sumOfdights =0
while no>0:
    sumOfrevers = (sumOfrevers*10) + (no%10)
    sumOfdights = sumOfdights +  (no%10)
    no = no//10
    count = count +1
    
print(sumOfrevers)
print(count)
print(sumOfdights)

if sumOfrevers==no2:
    print('Palindrame')
else:
    print('Not Palindrame')
    