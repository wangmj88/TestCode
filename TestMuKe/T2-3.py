from random import randint
d = {k:randint(50,100) for k in 'abcdefgh'}
print(d)
l =[(v,k) for k,v in d.items()]
print(l)
print(sorted(l,reverse = True))
print('#'*20)
print(sorted(list(zip(d.values(),d.keys())),reverse = True))

print(sorted(d.items(),key = lambda x:x[1],reverse=True))