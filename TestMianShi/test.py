#删除重复元素
listA = ['python','语','言','是','一','门','动','态','语','言']
for i in set(listA):
    print(i)

import collections
l =[item for item ,count in  collections.Counter(listA).items() if count == 1]
print(l)

#python 字典排序
dic = {'a':3 , 'b':2 , 'c': 1,'d':3,'e':5}
d =sorted(dic.items(),key=lambda asd:asd[0])
print(d)


#python如何删除dict中重复value值的item https://segmentfault.com/q/1010000000123481
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

