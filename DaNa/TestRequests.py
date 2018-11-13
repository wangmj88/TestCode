import requests
#传参
payload = {'key1': 'value1', 'key2': 'value2', 'key3': None}
r = requests.get('http://httpbin.org/get', params=payload)

print(r.url)
print(r'r.text#######返回headers中的变慢解析结果，可以通过rencoding = \'gbk\'来变更解码方式'.center(80,'*'))
print(r.text)

print('#r.content 返回二进制结果'.center(180,'='))
print(r.content)

print('r.json#返回JSON格式，可能抛出异常'.center(180,'*'))
print(r.json)

print('r.status_code'.center(180,'-'))
print(r.status_code)

print('#返回原始socket respons,需要加参数stream = True'.center(180,'*'))
r = requests.get('https://api.github.com/events', stream=True)
print(r.raw)

#参数也可以传递列表
payload = {"key1": 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get',params = payload)
print('r.url'.center(180,'*'))
print(r.url)

'''
#将结果保存到文件，利用r.iter_content()
with open(filename,'wb') as fd:
    for chunk in r.iter_content(chunk_size):
        fd.write(chunk)
'''

'''
#传递headers
url = 'httpbin.org/cookies'
headers = {'user-adent':'my-app/0/01'}
r1 = requests.get(url,headers = headers)
'''

#传递cookies
print('传递cookies'.center(180,'*'))
url = 'http://httpbin.org/cookies'
r = requests.get(url= url,cookies = dict(cookies_are = 'working'))
print(r.text)

#传递表单
print('传递表单'.center(180,'='))
r = requests.post('http://httpbin.org/post',data = {'key':'value'})
print(r.text)
print(r.json())

'''
    通常，你想要发送一些编码为表单形式的数据-非常像一个HTML表单。要实现这个，只需简单地传递一个自动给data参数。你的数据字典在发出请求时会自动编码为表单形式：
'''
payload = {'key1':'value1','key2':'value2'}
r = requests.post('http://httpbin.org/post',data = payload)
print(r.json())

'''
    很多时候你想要发送的数据并非表单形式的，如果你传递一个string而不是dict，那么数据会被直接发布出去。
'''
import json
url = 'https://api.github.com/some/endpoint'
payload = {'some':'data'}
r = requests.post(url,data=json.dumps(payload))
print(r.json())

#或者
r = requests.post(url,json = payload)
print(r.json())

#传递文件
url = 'http://httpbin.org/post'
file = {'file':open('report.xls','rb')}
files = {'file':('report.xls',open('report.xls','rb'),'application/vnd.ms-excel',{'Expires':'0'})}
files = {'file':('report.csv','some,data,to,send\nanother,row,to,send\n')}

r = requests.post(url,files = files)
print(r.status_code)

#跳转
r = requests.get('http://httpbin.org/cookies/set?k2 = v2 & k1 = v1')
print(r.url)
print(r.status_code)
print(r.history)

#高级特性
'''
    session ,自动保存cookies,可以设置请求参数，下次请求自动带上请求参数
'''
print('高级特性'.center(180,'*'))
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
'''
    session可以用来提供默认数据，函数参数基本的数据会和session级别的数据合并，如果key数据合并，如果key重复，函数参数级别的数据将覆盖session级别的数据。如果
    想取消session的某个参数，可以在传递一个相同key,value为None的dict
'''


