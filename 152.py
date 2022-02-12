d = {}

print(type(d))


d[1234] = 'selin'
d[1235] = 'elangovan'
d[1236] = 'ruban'
d[1237] = 'selin'

print(d)


d[1237] = 'sriruban'

print(d)

d[100] = 'kishantha'

print(d)


del d[1237]
print(d)

#d.clear()

print(d)

print(len(d))

print(d.get(1234))

#print(d.get(123))
print(d)

print(d.popitem())
print(d)


d = {1234:[60,70,80,90],1235:[50,65,75,85,],1236:[55,65,85,95],1237:[90,85,75,85]}

print(d.keys())
print(d.values())

print(type(d.keys()))
# d = {'celin':['abc','kandy',('abcd',True),'xyz']}

# print(d)


for key in d.keys():
    print(key)
    
for value in d.values():
    print(value)


for item in d.items():
    print(item)
    print(type(item))
    