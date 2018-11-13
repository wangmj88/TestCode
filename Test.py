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


