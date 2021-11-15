name1 = 'srikishantharuban'
name2 = "srikishantharuban"
print(name1)
print(name2)
address = '''srikishantharuban
           kandy'''
           
adress1 = 'srikishantharuban\n kandy'           
           
print(address)
print(adress1)



fileLoc = r'c:\new\file\music.mp3'
print(fileLoc)


sentamce = '''i'm fine '''
print(sentamce)


#string slicing
name = 'landscape'
print('front work indexing')
print(name[0],end = '*')
print(name[1],end ='*')
print(name[2],end ='*')
print(name[3],end ='*')
print(name[4],end ='*')
print(name[5],end ='*')
print(name[6],end ='*')
print(name[7],end ='*')
print(name[8],end ='*')
#print(name[9])
print("\n ------------------------------")
print('backword indexing')

print(name[-9],end = '*')
print(name[-8],end ='*')
print(name[-7],end ='*')
print(name[-6],end ='*')
print(name[-5],end ='*')
print(name[-4],end ='*')
print(name[-3],end ='*')
print(name[-2],end ='*')
print(name[-1],end ='*')

print()


#name = input('Enter your name:')
#print(name[0])
#print(name[-1])


alphapets = 'abcdefghijklmnopqrstuvwxyz'
#print('first five letters are:',alphapets [0:5])
#print('last five letter:',alphapets[-5:-1])
print(alphapets [0:])
print(alphapets[5:])

print(alphapets [:5])
print(alphapets[5:10])


print(alphapets [-1:])
print(alphapets[-5:])


print(alphapets[::2])
print(alphapets[::3])
print(alphapets[::4])
print(alphapets[::5])


print(alphapets[::1])
print(alphapets[-26:-1:2])
print(alphapets[0:10:3])
print(alphapets[5:25:4])


print('+++++++++++++++++++++++++++++++++++++++++++')

print(alphapets[-26:-1:-2])
print(alphapets[0:26:-2])



name = "lubtub"
print(name*5)

name ="kumaran"
fathername='raja'

print(name+fathername)

print('chennai'+'600028')
print('chennai',600028)


name = input('enter your name:')
lenth =len(name)
print(lenth)

name= input('Enter your name:')
print(len(name))

print(name[0].upper() + name[1:-1] + name[-1].upper())
