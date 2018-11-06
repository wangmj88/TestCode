#reduce()函数会对参数序列中元素进行积累。
'''
    函数将一个数据集合(链表，元组）中的所有数据进行下列操作：用传给reduce中的函数function(有两个参数）先对集合中的第1，2
    个元素进行操作，得到的结果再与第三个数据用function函数运算，最后得到一个结果。
'''
'''
    语法
    reduce(function,iterable[,initalizer])
   参数
   function--函数，有两个参数
   iterable--可迭代对象
   initializer--可选，初始化参数 
'''
from functools import reduce
def add(x,y):
    return x + y
print(reduce(add,[1, 2, 3, 4, 5]))

#filter
'''
   和map 类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值
   是True还是False决定保留还是丢弃该元素。
'''
#例如，在一个list中，删掉偶数，只保留奇数，可以这么写
def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(L)
#把一个序列中的空字符串删除，可以这么写：
def not_empty(s):
    return s and s.strip()
L = list(filter(not_empty,['A', '', 'B', None, 'C', ' ']))
print(L)

#sorted
l = sorted(['bob', 'about', 'zoo', 'Credit'],key = str.lower)
print(l)

l = sorted(['bob', 'about', 'Zoo', 'Credit'],key = str.lower, reverse = True)
print(l)

import operator
L = [('Bob',75), ('Adam',92), ('Bart',66), ('Lisa',88)]
print(sorted(L,key  =  lambda k:k[0]))
print('&'*100)
print(sorted(L,key  =  operator.itemgetter(0)))