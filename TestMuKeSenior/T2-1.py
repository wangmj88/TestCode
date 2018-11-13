from random import randint
#找出正数
l =[randint(-10,10) for x in range(10)]
print(l)
l1 =[x for x in l if x > 0]
print(l1)#[1, 1, 5, 7]
print('+'*10)
g = filter(lambda x:x > 0,l)
while True:
    try:
        la = next(g)
        print(la)
    except  StopIteration:
        print('到底了')
        break
'''
1
1
5
7
到底了
'''

#字典解析
d = {'student %s'%i:randint(50,100) for i in range(1,11)}
d_new = {k:v for k,v in d.items() if v > 60}
print(d_new)#{'student 4': 88, 'student 5': 79, 'student 7': 92, 'student 8': 93, 'student 9': 80, 'student 10': 93}
print('='*10)
g = filter(lambda item:item[1] > 60,d.items())
print(dict(g))#{'student 4': 88, 'student 5': 79, 'student 7': 92, 'student 8': 93, 'student 9': 80, 'student 10': 93}