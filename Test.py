#字典解析
from random import randint
d = {'student %i' %i:randint(50,100) for i in range(1,10)}
for k,v in d.items():
    if v > 70:
        print(k,v)

print('+'*10)
print({k:v for k,v in d.items() if v > 70})

g = filter(lambda item:item[1] > 70,d.items())
print(dict(g))