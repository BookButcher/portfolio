a = '10'
b = int(a)
b + 10
print(b)

b * 10
a * 10

v = float("10")
type(v)
print(v)

c = str(10)
print(c)

mylist = ['a', 'b', 'c']
z = mylist[1]
print(z)

d = mylist.index('b')
print(d)

e = dir(list)
print(e)

mylist.__setitem__(1, 'test')
print(mylist)

mylist[1] = 'e'
print(mylist)

e = mylist.__getitem__(1)
print(e)