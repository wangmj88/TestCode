classmates = ['Michael','Bob','Tracy']
print ('classmates = %s' % classmates)
langer = len(classmates)
print ('len(classmates) = %s' % langer)

#用索引来访问list中每一个位置的元素，记得索引是从0开始的
print('classmates[0] = %s' % classmates[0])

#当索引超出了范围时，Python会报一个IndexError 错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates)-1
#如果要取最后一个元素，除了机身索引位置外，还可以用-1做索引，直接获取最后一个元素
print('classmates[-1] =  %s' % classmates[-1])

#list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print('classmates = %s' % classmates)

#也可以把元素插入到指定的位置，比如索引号为1位置
classmates.insert(1,'Jack')
print('classmates = %s' % classmates)

#要删除list 末尾的元素，用pop()方法
print('classmates.pop() = %s' % classmates.pop())
print('classmates = %s' % classmates)

#要删除指定位置的元素,用pop(i)方法，其中i是索引位置:
print('classmates.pop(1) = %s' % classmates.pop(1))
print('classmates = %s' % classmates)

#要把某个元素换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print('classmates = :%s' % classmates)

#list元素的数据类型也可以不同，比如:
L = ['Apple', 123, True]
print('L = %s' % L)

#list元素也可以是另一个list，比如:
s = ['python', 'java', ['asp', 'php'], 'scheme']
print('len(s) = %s' % len(s))



