#tuple 另一种有序列表叫元组，tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
classmates = ('Michael', 'Bob', 'Tracy')
#现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常的
#使用classmates[0],classmates[-1],但不能赋值成另外的元素。
#不可变得tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽可能用tuple
#tuple陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须确定下来，比如：
t = (1, 2)
print(t)
#定义一个只有1个元素的tuple
t = (1,)
print(t)
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

L = [
    [
        'Apple', 'Google', 'Microsoft'
    ],
    [
        'Java', 'Python', 'Ruby', 'PHP'
    ],
    [
        'Adam', 'Bart', 'Lisa'
    ]
]
print(L[0][1])

#创建元组（只有一个元素时，在元素后面加上逗号）
tup = (1,)
print(tup)
print(type(tup))

#创建元组 （只有一个元素时，在元素后面加上逗号）
tup = (1)
print(tup)
print(type(tup))

#创建元组（多个元素）
tup = (1, 2, ["a", "b", "c"], "a")
print(tup)

#将列表转化为元组
list_name = ["python book", "Mac", "bile", "kindle"]
tup = tuple(list_name)
print(type(list_name))
print(type(tup))
print(tup)

#查询
tup = (1, 2, ['a', 'b', 'c'], 'd', 'e', ('gu', 'tang'))
print("tup[0] =", tup[0])

print("tup[1:] = ", tup[1:])#从索引为1到最后一个元素

print("tup[:-1] = ", tup[:-1])#到倒数第二个元素但不包含第二个

print("tup[1::1] = ", tup[1::1])#等价于tup[1:] 从左到右一个个去取，步长为1

print("tup[::-2] = ",tup[::-2])#反向输出 步长为2（隔一个去取）

#del 删除（元素对象不支持删除，但是可以删除整个元素变量）
#del删除元组中元素

tup = ('tang', 'guo', 'li', 'xiu')
del tup
# print(tup)

#count 统计元素个数
tup = ('tang', 'guo', 'li', 'xiu', 'guo').count('guo')
print(tup)

#index 返回元素的索引位置
tup = ('tang', 'guo', 'li', 'xiu').index('li')
print(tup)

'''
1,当元组中一个元素时，一定要在元素后面加上逗号
2，元组中的元素是不允许删除的，但可以使用del语句来删除整个元组
3，元组没有列表中的增，删，改的操作，只有查的操作
'''




