t1 = (10,20,30)
t2 = (5,10,15)
t3 = (t1 )+ (t2)
print(t3)
print(len(t3))
print(t3.count(10))
print(t3.index(10))

t5 = sorted(t3)
print(t5)


t5 = sorted(t3,reverse = True)

print(t5)

print(min(t5))

print(max(t5))

print(sum(t5))


#tuple packin and unpacking

a,b,c,d = 10,20,30,40

t = a,b,c,d

print(t)

q,r,s,t = t


# tuple comparstion

t = (i**i for i in range(1,6))
print(t)
print(type(t))

for value in t:
    print(value)
    