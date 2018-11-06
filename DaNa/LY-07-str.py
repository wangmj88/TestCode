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
