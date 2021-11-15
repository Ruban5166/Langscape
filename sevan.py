state1 = 'tamilnadu'
state2 = 'tamilnadu'

print(id(state1))
print(id(state2))


state1 = 'tamilnadu'
state2 = 'kerala'

print(id(state1))
print(id(state2))

print('hi hello')
print('hi\nHello')
print('hi\thello')
print('hi\hello')
print('I\'m Srikishantharuban')



print(5+10)
print(10-5)
print(10*5)
print(10/5)
print(10//5)
print(10/3)
print(10//3)
print(10%3)
print(10%4)
print(10**2)
print(10**3)
print(3**2)



print(10>5)
print(5>10)
print(100>=10)
print(100>99)
print(100>100)
print(200<100)
print(200<=200)
print(200<=500)


name1 = 'abcde'
name2 = 'abcd'

print(name1>name2)

#chaining oprators

print(10<20<30)
print(10<20>15)
print(10<20>30)



#equality oprators
print(10!=100)
print(20==100)

print(10==10==200)
print(10!=10!=100)



#logical oparators
#and or not

a = False
b = not a

print(b)



#Membership oprators
# in not in

sentance ='channi is capital of tamilnadu'
print('channi' in sentance)

subjacts = ['tamil','english','maths','science']
print('social' in subjacts)



#ternary oprators

a,b = 100,20
c = 30 if a> b else 40
print(c)



a = 1000
b = 2000
c = 300

min =a if a<b and a<c else b if b<a and b<c  else c 
print(min)

#identity oparators
#is is not
a = 10
b = 10

print(a==b) # content comparetor
print(a is b) # memory comparetor

a = input('enter the number1:')
b = input('enter the number2:')
c = input('enter the number3:')

max = a if a>b and a>c else b if b>a and b>c  else c

print(max)


















