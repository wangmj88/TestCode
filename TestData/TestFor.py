#循环
#要计算1+2+3，我们可以直接写表达式：
#1+2+3
#python 的循环有两种，一种是for...in 循环，依次把list或tuple中的每个元素迭代出来，看例子
names = ['Michael', 'Bob', 'Tray']
for name in names:
    print(name)

#所以for x in ... 循环就是把每个元素代入变量x，然后执行缩进块的语句
#再比如我们想计算1-10的整数之和，可以用一个，sum变量做累加

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

#如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list（）函数可以转换为list.
#比如range(5) 生成的序列是从0开始小于5的整数

print(list(range(5)))
print(list(range(1,5)))

#第二种循环是while循环，只要满足条件，就不断循环，条件不满足时退出循环，比如我们要计算100以内所有奇数之和，可以用while循环实现
sum = 0
n = 99
while n > 0:
    sum = sum +n
    n = n -2
print(sum)

#请利用循环依次对list中每个名字打印出Hell,xxx！
L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print("Hello", i)

#break
#在循环中，break语句可以提前退出循环。例如，本来要循环打印1-100的数字：
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

#如果要提前结束循环，可以用break语句:
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

#continue
#在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue#continue 语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)


