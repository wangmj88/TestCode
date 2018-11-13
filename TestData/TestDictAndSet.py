#dict
#Python 内置了知道：dict的支持
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

#把数据放入dict的方法，除了初始化时指定外还可以通过key放入
d['Adam'] = 67
print(d)

#由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的冲掉
#要避免key不存在的错误，有两种方法，一是通过in判断key是否存在：
if 'Thomas' in d :
    print('True')
else:
    print('False')

#而是通过dict提供的get()方法，如果key不存在，key返回None，或者自己指定的value:
print(d.get('Thomas', -1))
#注意返回None的时候Python 的交互环境不显示结果.
#要删除一个key,用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')
print(d)

#请注意，dict内部存放的顺序和key放入的顺序是没有关系的。
#和list比较，dict有以下几个特点
'''
1,查找和插入的时间随着元素的增加而变慢
2，需要占用大学的内存，内存浪费
多
'''

#set
'''
set 和 dict 类似，也是一组key的集合，但不存储value.由于key不能重复，所以在set中，没有重复的key
要创建一个set,需要提供一个list作为输入集合
'''

s = set([1,2,3])
print(s)
print(type(s))

'''
注意，传入的参数[1，2，3]是一个list ，而显示的{1,2,3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。
重复元素在set中自动被过滤：
'''

s = set([1,1,2,2,3,3])
print(s)

'''通过add(key)方法添加元素到set中，可以重复添加，但不会有效果'''
s.add(4)
print(s)
s.add(4)
print(4)

'''通过remove(key)方法可以删除元素'''
s.remove(4)
print(s)

'''set 可以看出数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集，并集，等操作'''
s1 = set([1,2,3])
s2 = set([2,3,4])

print(s1 & s2)
print(s1 | s2)

'''set 和 dict 的唯一区别仅在于没有存储对应的value,但是，set的原来和dict一样，所以，同样不可以放入可变对象，因为无法判断
两个可变对象是否相等，业务就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错'''

'''再议不可变对象'''
'''上面我们讲了，str是不可变对象，而list内部的内容是会变好的，比如'''
a = ['c', 'b', 'a']
a.sort()
print(a)
'''而对于不可变对象，比如str,对str进行操作呢'''
a = 'abc'
a.replace('a','A')
print(a)
print(a.replace('a','A'))

'''虽然字符串有个replace()方法，也确实变出了’Abc',但是变量a最后仍是'abc'，应该怎么解释呢？'''
a = 'abc'
b = a.replace('a','A')
print(b)
print(a)

a = (1, 2, 3)
b = (1, [2,3])
a1 = set(a)
print(a1)

