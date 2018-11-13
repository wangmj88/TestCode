#python 字典排序
dic = {'a':3 , 'b':2 , 'c': 1,'d':3,'e':5}
print(sorted(dic.items(),key = lambda asd:asd[0],reverse = True))
print(sorted(dic.items(),key = lambda asd:asd[1],reverse = True))

print('split ------------------------------------------------------')
#python如何删除dict中重复value值的item https://segmentfault.com/q/1010000000123481
#思路 把dict中每项的key:value先翻转，自然形成一个去掉重复value的dict，再多翻转一次
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
print(a) #{3: 'a', 4: 'b', 6: 'c', 7: 'd'}
print('*'*100)
func = lambda a:dict([(x, y) for y, x in a.items()])
print (func(func(a))) #{3: 'a', 4: 'b', 6: 'c', 7: 'd'}
print(func(a))#{'a': 3, 'b': 4, 'c': 6, 'd': 7}
