name = input('Enter you name:')
print(len(name))


mid = (len(name)//2)
print(mid)
print(name[0:mid])
print(name[mid].upper())
print(name[mid+1:])


print((name[0:mid])+(name[mid].upper())+(name[mid+1:]))





