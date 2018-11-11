关于REQUEST请求和SESSION请求的区别
1.session访问(带header，带body)

s=request.session()

s.headers.update()#header直接在session中更新

r2=s.post(url,data=body)

2.request访问

r=request.post(url,headers=h,data=body)

3.

应该是有body都是post请求，post请求不一定都有body

应该是有body都是post请求，post请求不一定都有body

4.data,param的区别

python之使用request模块发送post和get请求
import requests
import json

#发送get请求并得到结果
# url = ‘http://api.nnzhp.cn/api/user/stu_info?stu_name=小黑马 ‘#请求接口
# req = requests.get(url)#发送请求
# print(req.text)#获取请求，得到的是json格式
# print(req.json())#获取请求，得到的是字典格式
# print(type(req.text))
# print(type(req.json()))

#发送post请求,注册接口
# url = ‘http://api.nnzhp.cn/api/user/user_reg‘
# data = {‘username‘:‘mpp0130‘,‘pwd‘:‘Mp123456‘,‘cpwd‘:‘Mp123456‘}
# req = requests.post(url,data)#发送post请求，第一个参数是URL，第二个参数是请求数据
# print(req.json())

#入参是json
# url = ‘http://api.nnzhp.cn/api/user/add_stu‘
# data = {‘name‘:‘mapeipei‘,‘grade‘:‘Mp123456‘,‘phone‘:15601301234}
# req = requests.post(url,json=data)
# print(req.json())

#添加header
# url = ‘http://api.nnzhp.cn/api/user/all_stu‘
# header = {‘Referer‘:‘http://api.nnzhp.cn/‘}
# res = requests.get(url,headers=header)
# print(res.json())

# 添加cookie
# url = ‘http://api.nnzhp.cn/api/user/gold_add‘
# data = {‘stu_id‘:231,‘gold‘:123}
# cookie = {‘niuhanyang‘:‘7e4c46e5790ca7d5165eb32d0a895ab1‘}
# req = requests.post(url,data,cookies=cookie)
# print(req.json())

#上传文件
# url = ‘http://api.nnzhp.cn/api/file/file_upload‘
# f = open(r‘E:\besttest\te\python-mpp\day7\练习\11.jpg‘,‘rb‘)
# r = requests.post(url,files={‘file‘:f})
# users_dic = r.json()
# print(users_dic)

# 下载文件
# url = ‘http://www.besttest.cn/data/upload/201710/f_36b1c59ecf3b8ff5b0acaf2ea42bafe0.jpg‘
# r = requests.get(url)
# print(r.status_code)#获取请求的状态码
# print(r.content)#获取返回结果的二进制格式
# fw = open(‘mpp.jpg‘,‘wb‘)
# fw.write(r.content)
# fw.close()

#把浏览器页面下载到本地   保存网页，可以理解为简单的爬虫工具
url=‘http://www.nnzhp.cn/archives/630‘
r = requests.get(url)
f = open(‘nnzhp.html‘,‘wb‘)
f.write(r.content)
f.close()