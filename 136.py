# set

s ={ 10,20,30,40}


l = [10,10,10,20,20,30,30,30,]
s = set(l)
print(s)

s = set(range(5))
print(s)

s = set()
print(s)

#---------------------------------------------

t = tuple()
print(type(t))


name = 'srikishantharuban'
s = set(name)
print(s)
t = tuple(name)
print(t)
l = list(name)
print(l)

#------------------------------------------------------------------------------
l = (10,20,30,40,50,60,70)
s = {100,200,300,400,500,600,700}


s.update(l,range(5))
print(s)


s2 = s.copy()
print(s2)

s.remove(600)
print(s)

s.discard(700)



s1 = {10,20,30,40,50}
s2 = {30,40,50,60,70}

print(s1.union(s2))

print(s1 & s2)
print(s1 -s2)
print(s2 -s1)

print(s2^s1)


s= frozenset(s2)