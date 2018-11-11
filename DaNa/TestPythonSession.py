#https://www.cnblogs.com/jason89/p/9033949.html
#https://blog.csdn.net/shanzhizi/article/details/50903748
#https://www.cnblogs.com/BlueSkyyj/p/7594533.html
import requests
'''
def login():
'''
    #登录接口:/auth/login
'''
    s = requests.Session()
    r = s.post(url = 'http://11x.39.63.xx:20080/auth/login',
               data = {'username':'system',
               'password':'123456'}
               )
    return s

def selectable():
    r = login().get(
        url = 'http://11x.39.63.xx:20080/depot/parks/selectable'
    )
    print(r.status_code)
    print(r.text)

selectable()
'''

def login():
    s = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    url = 'https://passport.baidu.com/v2/api/?login'
    data = {'staticpage':'https://www.baidu.com/cache/user/html/v3Jump.html',
            'charset':'UTF-8',
            'token':'58fa2359e66150b6ce75dc1bd998912c',
            'tpl':'mn',
            'subpro':'',
            'apiver':'v3',
            'tt':'1541905519587',
            'codestring':'',
            'safeflg':'0',
            'u':'https://www.baidu.com/',
            'isPhone':'',
            'detect':1,
            'gid':'8D953FD-2E65-4035-B5C2-FB408E966A9D',
            'quick_user':0,
            'logintype':'dialogLogin',
            'logLoginType':'pc_loginDialog',
            'idc':'',
            'loginmerge':'true',
            'splogin':'rate',
            'username':'13552378756',
            'password':'ITh0Tq6ucqAFFLxmnx3FscwKZgCgLU1xJCPXtyb7obeceedMDVObn6rth09bsSmInc6k1losmVl1I3E63Y3h7OPkLZFP8od7bVSjkVMNqxVZONvDF5QB1vP2iWPeONaJEwyKDSkv+Mph1yX02wHCtBfx3eJABFcIObqMr8ykqJ0=',
            'rsakey':'m8PeyWuIKAEWQeVKIlwZbI8yNGlf9tD5',
            'crypttype':12,
            'ppui_logintime':50377,
            'countrycode':'',
            'fp_uid':'',
            'fp_info':'',
            'loginversion':'v4',
            'dv':'tk0.09315662521021141541905469317@wwr0~CBk3G8muIDI-nI3vBKxdDIxhN80hNKXC~FKs75JxZok2x7kruNkIuokqGC2v7Exsh0CdNIvBDK~2wKxdxAzCa0TvfFHwuBPqy7nwx8awwovEh03OHDIxNKxh0IvWu8vdNOKBZA3-RMJIG805~80OWB08G8muIDI-nI3vBKxdDIxhN80hNKXC~FKs75JxZok2zB0qXNkIwokqGC2v7Exsh0CdNIvBDK~2wKxdxAzCa0TvfFHwuBPAzBUw_mr0wm7kDXok2yB1wu8k3jonwz7kDG8~3xokru7kDGNkI-Bmwx80tG8~2~8HuIDI-nI3vBKxdDIxhN80hNKzFeMXEZAZC8MzOQM3syMUwxBP3G8~DzokI~8~qGC2v7Exsh0CdNIvBDK~2wKxdTMXsfNkAxBmwy8PtGB~DuBmuWCggLugzdw--Mhzrh8HwaokAwxrQOpGwoPq-8~2xBP5aB0ru8kru80DuB0Du70qxBk5-8~2XhrQLnEyAn8boadXOXAi5TvQFnIi5zdfoauxMTEZFTZiFJD_Irl8mwwok2~BP5GBPIXok2~BP5GB~5jok2~BP5G808zB1wX8Pt_',
            'traceid':'13C45901',
            'callback':'parent.bd__pcbs__927z31'
            }
    r = s.post(url = url,json = data,headers = headers,verify = False)
    # print(r.status_code)
    # print(r.text)
    # print(r.content)
    # print(r.ok)
    # print(r.url)
    return s
def selectable():
    s = login()
    url = 'https://hm.baidu.com/hm.gif?cc=0&ck=1&cl=24-bit&ds=1366x768&vl=657&ep=46426%2C2950&et=3&ja=0&ln=zh-cn&lo=0&lt=1541907363&rnd=1492799424&si=4010fd5075fcfe46a16ec4cb65e02f04&su=https%3A%2F%2Fwww.baidu.com%2F&v=1.2.35&lv=2&sn=65418'
    data = {'cc':0,
            'ck':1,
            'cl':'24-bit',
            'ds':'1366x768',
            'vl':657,
            'ep':(46426,2950),
            'et':3,
            'ja':0,
            'ln':'zh-cn',
            'lo':0,
            'lt':'1541907363',
            'rnd':'1492799424',
            'si':'4010fd5075fcfe46a16ec4cb65e02f04',
            'su':'https://www.baidu.com/',
            'v':'1.2.35',
            'lv':2,
            'sn':65418
            }

    r = s.get(url = url)
    print(r.status_code)
    print('r.status_code'.center(200,'*'))
    # r.encoding = 'utf-8'  # 这里添加一行
    print(r.encoding)
    print('r.status_code'.center(200, '*'))
    print(r.text)

selectable()