#条件判断
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
#根据Python的缩进规则，如果if语句判断是True,就把缩进的print语句执行了，否则，什么也不做:
#也可以给if添加一个else语句，意思是，如果if判断是False,不要执行if的内容，去把else执行了:
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')

#注意不要少写了冒号:
#当然上面的判断是很粗略的，完全可以用elif做更细致的判断
age = 3
if age >= 18:
    print('adult')
elif age >=6:
    print('teenager')
else:
    print('kid')

#if 语句执行有个特点，它是从上往下判断，如果在某个判断上是True,把该判断对应的语句执行后，就忽略掉剩下的elif和else,
#所以请测试并解释为什么下面的程序打印的是teeager:
print('*'*50)
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

#if 判断条件还可以简写，比如写：
#只要X是非零数值，非空字符串，非空list等，就判断为True,否则为False.
x = 1
if x:
    print('True')

#再议input
#最后看一个有问题的条件判断，很多同学会用input()读取用户的输入，这样可以自己输入，程序运行的更有意思：
s = input('birth：')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

#练习
'''
小明身高1.75，体重80.5kg。根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
低于 18.5 过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断打印结果
'''
print("练习".center(50,('*')))
height = 1.75
weight = 80.5
BMI = weight/(height*height)
if BMI < 18.5:
    print("过轻")
elif BMI >= 18.5 and BMI < 25:
    print("正常")
elif BMI >= 25 and BMI < 32:
    print("肥胖")
else:
    print("严重肥胖")



