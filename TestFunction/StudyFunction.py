#max函数max()可以接收任意多个参数，并返回最大的那个
a = max(1, 2)
print(a)

#数据类型转换
#Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
a = int('123')
print(a)
a = float('12.34')
print(a)
a = str(1.23)
print(a)
a = str(100)
print(a)
a = bool(1)
print(a)

#在python中，定义一个函数要使用def语句，依次写出函数名，括号，括号中的参数和冒号：，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
#我们定义一个求绝对值的my_abs函数为例
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))

'''
    请注意，函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑
    如果没有return语句，函数执行完毕后也会返回结果，只是结果为None,return None可以简写为return.
    在python交互环境中定义函数时，注意python会出现...的提示。函数定义结束后需要按两次回车重新回到>>提示符下
'''

'''
    参数检查调研函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
    但是如果参数类型不对，Python 解释器就无法帮我们检查。
    让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点类型的参数，数据类型检查可以内置函数isinstance()实现：
'''
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# my_abs('A')

'''
    返回多个值
    
'''
import math
def move(x,y,step,angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi / 6)
print(x,y)

#可变参数
'''
    在pthon函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变，可以是1个，2个到任意个，还可以是0个
    我们以数学题为例子，给定一组数字a,b,c...，请计算
    要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a,b,c...作为一个list或tuple传进来，
    这样，函数就可以定义如下：
'''
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
'''
    但是调用的时候，需要先组装出一个list和tuple:
'''
print(calc([1,2,3]))
print(calc((1,3,5,7)))

'''
    如果利用可变参数，调用函数的方式可以简化成这样：calc(1,2,3)
'''
#所以我们把函数的参数改为可变参数：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
''''
    定义可变参数和定义一个list参数相比，仅仅在参数前面加了一个*号，在函数内部，参数numbers接收到额是一个tuple,
    因此，函数代码完全不变。但是，调用函数时，可以传入任意个参数，包括0个参数
'''
print(calc(1, 2, 3))
print(calc())

'''
    如果有一个list或者tuple，要调用一个可变参数怎么办?可以这样做：
'''
nums = [1,2,3]
print(calc(nums[0],nums[1],nums[2]))

'''
 这种方法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前加一个*号，把list或tuple的元素变成可变参数传进去
'''
print('*'*100)
nums = [1,2,3]
print(calc(*nums))
'''
    *nums 表示把nums这个list的所有元素作为可变参数传进去，这种写法相当有用，而且很常见
'''

'''
    关键字参数
    可变参数允许你传入0个人或者任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个
    或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict.请看示例：
'''
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
'''
    函数person除了必选参数name和age外，还接受关键字参数kw.在调用该函数时，可以值传入必选参数：
'''
print('='*100)
person('Michael',30)
'''
    也可以传入任意个数的关键字参数
'''
person('Bob',35,city = 'BeiJing')
person('Adam',45,gender = 'M',job = 'Engineer')

#当然，上面复杂的调用可以用简化的写法
extra = {'city':'Beijing','job':'Engineer'}
person('Jack',24,**extra)

#命名关键字参数
'''
    对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查
    仍以person()函数为例，我们希望检查是否有city和job参数：
'''
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
person('Jack',24,city = 'Beijng',addr = 'Chaoyang',zipcode = 123456)

'''
    如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接受city和job作为关键字参数。这种方式定义的函数如下：
'''
def person(name,age,*,city,job):
    print(name,age,city,job)
'''
    和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    调取方式如下：
'''
person('Jack',24,city='Beijing',job='Engineer')

'''
    如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不在需要一个特殊分隔符*了
'''
def person(name,age,*args,city,job):
    print(name,age,city,job)
'''
    命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
'''
# person('Jack',24,'Beijing','Engineer')

#命名关键字参数可以有缺省值，从而简化调用
def person(name,age,*,city = 'Beijing',job):
    print(name,age,city,job)
#由于命名关键字参数city具有默认值，调用时，可不传入city参数：
person('Jack',24,job = 'Engineer')






