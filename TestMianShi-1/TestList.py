#python 查找重复项
l = [1,2,3,2,1]
for i in l:
    print("this %s ha fount %s" %(i,l.count(i)))
print('split line----------------------------')
s = set(l)
for j in s:
    print("the %s has fount %s" %(j,l.count(j)))

#删除重复元素
listA = ['python','语','言','是','一','门','动','态','语','言']

print(sorted(set(listA)))

#[python] 查找列表中重复的元素
a = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
#写法1：
import collections
l =[item for item,count in collections.Counter(a).items() if count >1]
print(l)
print('collections.Counter(a).items()'.center(50,'*'))
print(collections.Counter(a).items())
print(collections.Counter(a))
l1 = [item for item ,count in collections.Counter(a).items() if count >1]