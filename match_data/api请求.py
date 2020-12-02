from urllib.parse import urlencode
import requests
apis = ['http://api.tianapi.com/txapi/saylove/index',
    'http://api.tianapi.com/txapi/gjmj/index',
    'http://api.tianapi.com/txapi/everyday/index',
    'http://api.tianapi.com/txapi/caihongpi/index',
    'http://api.tianapi.com/txapi/hsjz/index',
    'http://api.tianapi.com/txapi/pyqwenan/index',
    'http://api.tianapi.com/txapi/mgjuzi/index',
    'http://api.tianapi.com/txapi/dujitang/index',]

params = {
    'key': 'd98cb8d8c6f5ab4ee4705f18f8f889aa',
}
request_api = apis[1] + '?' +  urlencode(params)
r = requests.get(request_api)
print(r.json().get('newslist')[0].get('content'))
print(request_api)
