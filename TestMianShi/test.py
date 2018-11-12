l = [1,2,3,2,1]
for i in l:
    print("this %s has found %s"%(i,l.count(i)))
print('split line ------------------------')

s = set(l)
for j in s:
    print("this %s has fount %s" %(j,l.count(j)))