#list
#append() 向列表末尾添加新元素，返回None
list1 = [1,2,3,4,5]
list1.append(6)
print(list1)

#extend()将一个列表继承另一个列表
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = list1.extend(list2)
print('extend()'.ljust(50,'*'))
print(list1)
print(list2)
print(list3)
print(list1+list2)

#index 获取值在列表中的索引
list1 = [1,3,2,3,4,5,3]
print(list1.index(3))
print(list1.index(3,2,5))

#fromkeys()按照指定的序列为键创建字典，值都是一样的
list1 = ['a','b','c']

