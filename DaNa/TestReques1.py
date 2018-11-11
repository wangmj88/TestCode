import requests
s = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
url = 'http://httpbin.org/basic-auth/wangmj88/xiao0503'
# http://httpbin.org/hidden-basic-auth/wangmj88/xiao0503
# url = 'http://httpbin.org/hidden-basic-auth/wangmj88/xiao0503'
r = s.get(url = url, headers = headers ,auth = ('wangmj88', 'xiao0503'))
print(r.status_code)
print(r.text)

