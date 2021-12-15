list1 =[10,20,30,40,50,60,70,80,90,100]  
list2 = ['a','b','c','d','e']    


list3 =[list1,list2]

#print(list3)

for innerlist in list3:
    #print(innerlist)
    for elements in innerlist:
        if type(elements)==int:
            print(elements,end =' ')
        

