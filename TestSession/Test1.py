#参考文档 http://www.cnblogs.com/ddddfpxx/p/8624715.html

import requests
from PIL import Image
from io import BytesIO
def LoginByPost():
    imgUrl='http://***/authcode.php'
    s=requests.session()
    res=s.get(imgUrl,stream=True)
    im=Image.open(BytesIO(res.content))
    im.show()
    code=input()
    loginUrl='http://***/admin_loginCheck.php'
    postData={'pname':'admin','password':'***','validateCode':code}
    rs=s.post(loginUrl, postData)
    url='http://***/***/admin_honor.php'
    res=s.get(url)
    res.encoding='utf-8'
    print(res.text)
'''
此时，可以看出我们已经成功登录，并输出指定页面的内容。

2.利用Cookies直接登录。无需用户名、密码及验证码。此时，需要先获得登录该网站后的Cookies，一种方法是通过浏览器查看Cookies，另一种方法是利用上面的requests.session获取登录后的Cookies。我们采用第二种方式。
'''
#（1）通过requests.session获取Cookies。
def GetCookie():
    imgUrl='http://***/authcode.php'
    s=requests.session()
    print(s.cookies.get_dict())#先打印一下，此时一般应该是空的。
    res=s.get(imgUrl,stream=True)
    im=Image.open(BytesIO(res.content))
    im.show()
    code=input()
    loginUrl='http://***/admin_loginCheck.php'
    postData={'pname':'admin','password':'***','validateCode':code}
    rs=s.post(loginUrl,postData)
    c=requests.cookies.RequestsCookieJar()#利用RequestsCookieJar获取
    c.set('cookie-name','cookie-value')
    s.cookies.update(c)
    print(s.cookies.get_dict())

#（2）利用上面获取的Cookies直接登录
def DirLogin():
    s=requests.session()
    url='http://***/***/admin_honor.php'
    headers={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': '***',
    'Referer': 'http://***/***/admin_index.php'
    }
    cookies={'PHPSESSID': 'cnguud4r1hmn3passs906odp21'}#这里就是利用上面的函数获得的Cookies
    rs=s.get(url,headers=headers,cookies=cookies,verify=False)
    rs.encoding='utf-8'
    print(rs.text)

'''
    此时，可以直接查看所需要页面的内容。

说明：然并卵，你会发现，通过Cookies直接登录，有时好用，有时无用。原因在于此网站是通过服务器的Session对客户进行判断，而Session在服务器端往往会设置会话期限，如果到了时间，服务器会把这个Session删除，这时，你还得再次利用第一个函数进行Cookie的获取。
'''