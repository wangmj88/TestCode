s = 'i LOVE WangXiaoJing'
print(s.capitalize())
print(s.capitalize())
print(s.find('i',1))
print(s.index('i',0))
# print(s.index('w',0))
print(s.count('i'))
s = 'I like dog'
print('*'*100)
print(s.startswith('i'))
print(s.startswith('I'))

s = 'f狗gh'
s1 = 'DF狗GH'
#isupper(),检查所有字母是否是大写字母，返回的都是布尔值
print('='*80)
print(s.isupper())
print(s1.isupper())
#islower(),检测所有字母是否是小写字母
print('islower检测所有字母是否是小写字母'.center(50, '-'))
print(s.islower())
print(s1.islower())
#istitle()检测是否以指定标题显示（美国单纯受字母大写）
print('istitle() 检测是否以指定标题显示(每个单词首字母大写)'.center(50,'='))
print(s.istitle())
print(s1.istitle())
s2 = 'I Like Dog'
print(s2.istitle())
#isspance()检测字符串是否是空字符串
print('isspance()检测字符串是否是空字符串'.center(50,'*'))
s ='   '
s1 = 'i like'
s2 = ' '#至少有一个，否则返回false
print(s.isspace())
print(s1.isspace())
print(s2.isspace())
#isalpha()检测字符串是否是字母组成 返回布尔值
print(('isalpha()检测字符串是否是字母组成，返回布尔值').center(50, '-'))
s = 'I 狗like dog'
s1 = 'I狗likedog'
print(s.isalpha())
print(s1.isalpha())
#isdigit()检测字符串是否有数字组成
#isdecimal()
#isnumeric()
print(('isdigit()检测字符串是否有数字组成').center(30,'-'))
s = '123'
print(s.isdigit())
print(('isdecimal').center(50,'-'))
print(s.isdecimal)
print(('isnumeric').center(50,'*'))
print(s.isnumeric())

print(("b'101100'isdigit()").center(50,"*"))
s = b'101100'
print(s.isdigit())

s = 123.2
# print(s.isdigit())
# print(s.isdecimal())

#strip()去掉左右两边指定字符，默认是去掉空格
#lstrip()去掉左边指定字符，默认空格
#rstrip()去掉右边指定字符，默认空格
print(('strip()去掉左右两边指定字符，默认是去掉空格').center(50,'*'))
s = '    abc   '
print('---'+s.strip()+'---')
print('---'+s+'---')
#maketrans()生成用于字符串替换的映射表
#translate()进行字符串替换

print(('maketrance生成用于字符串替换的映射表').center(50,'-'))
s = '今天晚上我吃的是小炒肉，可好吃了'
table = s.maketrans('小炒肉', '大白菜')
print(table)
print(s.translate(table))
print(s.replace('小炒肉', '大白菜'))
print(s.translate(s.maketrans('小炒肉', '大白菜')))
