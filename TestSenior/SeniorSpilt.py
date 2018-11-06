#取一个list或者tuple的部分元素是非常常见的操作。比如，一个list如下：
L = ['Michael', 'Sarah', 'Tray', 'Bob', 'Jack']
#取前3个元素，应该怎么做？
#笨方法
print(L[0],L[1],L[2])
#之所以是笨方法，是因为扩展一下，取前N个元素就没辙了，取前N个元素，也就是索引为0-（N-1)的元素，可以循环：
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

#对这种经常取知道索引范围的操作，用循环是否繁琐，因此，python提供了切片（Slice)操作符，能大大简化这种操作。

print(L[0:3])

#如果第一个索引是0，还可以省略
print(L[:3])

#迭代
'''
    list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只有是可迭代对象，无论有无下标，都可以迭代，比如dic就可以迭代
'''
d = {'a':1,'b':2,'c':3}
for v in d.values():
    print(v)
'''
    因为dic存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
    默认情况下，dict迭代的是key,如果要迭代value,可以用for value in d.values(),
    如果要同事迭代key和value,可以用for k,v in d.items().
'''

'''
    由于字符串也是可迭代对象，因此，也可以作用于for循环：
'''
for ch in 'ABC':
    print(ch)

'''
    所以，当我们使用for循环时，只有作用于一个可迭代对象，for循环就可以正常运行，而我们不天关心
    该对象究竟是list还是其他数据类型。
    那么如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
'''
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance(1,int))
print(isinstance('abc',str))
'''
    最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中
    同事迭代索引和元素本身：
'''
for i,value in enumerate(['A','B','C']):
    print(i,value)

'''
    上面的for循环里，同事引用了两个变量，在Python里很常见，比如下面的代码
'''
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)

#列表生成式
'''
    列表生成式即ListComprehensions,是Python内置的非常简单却强大的key用来创建list的生成式。
'''
print(list(range(1,11)))
#如果要生成[1X1,2X2...10X10]
L = []
for i in range(1,11):
    L.append(i*i)
    print(L)
print(L)

'''
    但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list:
'''
L = [x * x for x in range(1,11)]
print('*'*100)
print(L)

'''
    还可以生成两层循环，可以生成全排列
'''
L =[m + n for m in 'ABC' for n in 'XYZ']
print(L)

'''
    列出当前目录下的所有文件和目录名，可以通过一行代码实现
'''
import os
L = [d for d in os.listdir('.')]
print(L)

'''
    for循环其实可以同时使用两个变量，比如dic和items()可以同时迭代key和value:
'''
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)

'''
因此，列表生成式，也可以使用两个变量来生成list
'''
print('='*100)
d = {'x':'A','y':'B','z':'C'}
L =[k + '=' + v for k ,v in d.items()]
print(L)

#生成器
g = (x * x for x in range(10))
print(g)
for i in g:
    print(i)

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n + 1
    return 'done'
fib(6)

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a + b
        n = n + 1
    return 'done'

g = fib(6)
while True:
    try:
        x = next(g)
        print('g',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b ,a + b
        n = n + 1
    return 'done'

g = fib(6)

while True:
    try:
        x = next(g)
        print('g',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

#迭代器
'''
    我们已经知道，可以直接作用于for 循环的数据类型有一些几种：
    一类是集合数据类型，如list,tuple,dict,set,str等；
    一类是generator,包括生成器和yield的generator function.
    这些可以直接作用于for循环的对象统称为迭代对象：Iterable.
    可以使用isinstance()判断一个对象是否是Iterable对象：
'''
from collections import Iterable


