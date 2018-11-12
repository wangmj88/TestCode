l = [1,2,3,2,1]
for i in l:
    print("this %s has found %s"%(i,l.count(i)))
print('split line ------------------------')

s = set(l)
for j in s:
    print("this %s has fount %s" %(j,l.count(j)))

a = {
    1: 'a',
    2: 'a',
    3: 'a',
    4: 'b',
    5: 'c',
    6: 'c',
    7: 'd'
}
b = {a[key]:key for key in a}
a = {b[key]:key for key in b}
print(a)
func = lambda a:dict([(x, y) for y, x in a.items()])
func = lambda a:dict([(x ,y) for y ,x in a.items()])
print(func(func(a)))