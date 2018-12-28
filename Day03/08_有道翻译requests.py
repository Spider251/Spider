import requests
import json
# 接收用户输入
key = input("请输入翻译的内容:")

# 把Form Data定义成一个字典
data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15458119967501',
        'sign': '65b4a3d84faa02b256b6bc3e2b112832',
        'ts': '1545811996750',
        'bv': '53850875da92527c18a78e804f4c65b4',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false'
}

# 把data转为bytes数据类型
# 发起请求, 获取响应, 获取内容
# 此处的URL地址为F12抓到的POST地址
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {'User-Agent':'Mozilla/5.0'}
# 此处使用post()方法
res = requests.post(url,data=data,headers=headers)
res.encoding='utf-8'
html = res.text
# 翻译的内容为translation变量
translation = eval(html)['translateResult'][0][0]['tgt']

# 把json格式的字符串转为python中的字典
rDict = json.loads(html)
translation1 = rDict['translateResult'][0][0]['tgt']
print(translation)