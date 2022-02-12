num = [1,3,5,7,9]

i = 0

num2 = []
#print(range(len(num)))
for i in range(len(num)):
   
    j = 1
    for j in range(0,len(num)):
        a = (i * 10) + num[j]
        num2.append(a)
        j = j+1
i = i = 1 

print(num2)