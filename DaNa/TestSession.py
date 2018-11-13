'''
    我们首先需要登录，登录成功后，可以获取XX的信息，见login接口响应恢复内容：
    {
        "code":200
    }
    在如上中可以看到，登录只返回了code是200,并没有期待的中的返回token，那么可以得知该系统使用的是session
    的方式来记住用户登录后的密钥，
    也就是说，执行login的接口后，首先需要到sessionID，在下一个接口请求中带上login返回的sessionID，否则执行就会出现401
    无权限的问题，那么
    我们先来执行login的接口，见实现的代码
'''
import requests
def login():
    '''
        登录接口:/auth/login
    :return:
    '''
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
# data = {'user':'wangmj88','passwd':'xiao0503'}
# r = requests.get(
#     url  = 'https://httpbin.org/basic-auth/',
#     data =data,
#     headers = headers,
#     verify = False
# )
# print(r.url)
# print(r.status_code)
# print(r.text)

import requests

r = requests.get(url='http://www.itwhy.org')  # 最基本的GET请求
print(r.status_code)  # 获取返回状态
r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})  # 带参数的GET请求
print(r.url)
