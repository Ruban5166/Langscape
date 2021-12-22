no1 = [100,200,300,400]
no2 = [300,400,500,600]

for i in no1:
    if i not in   no2:
        print(i)



no3 =[i for i in no1 if i not in no2]

print(no3)