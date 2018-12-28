from urllib.request import urlopen,Request
url = "http://www.renren.com/969267684/profile"

headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #Accept-Encoding: gzip, deflate
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Cookie':'td_cookie=18446744069553321175; anonymid=jq7ddbnovweuk9; depovince=GW; _r01_=1; JSESSIONID=abch4I6bpaJuF4dr4DYFw; ick_login=ecd059cc-4ffc-4f25-9479-56e6ccd72362; t=ad467198d5d6b8455b97d6f63e3feed24; societyguester=ad467198d5d6b8455b97d6f63e3feed24; id=969267684; xnsid=d8829b9; ver=7.0; loginfrom=null; jebe_key=02d85313-bfc5-444c-8ca6-8e1dfc4a865c%7C80e648859a5127a42b878ee000838f96%7C1545961200626%7C1%7C1545961200785; wp_fold=0; _ga=GA1.2.1589217031.1545961217; _gid=GA1.2.1605129198.1545961217; jebecookies=efd63ae7-ce0f-46ae-a165-d965d29cc9ce|||||',
    'Host':'www.renren.com',
    'Pragma':'no-cache',
    'Referer':'http://www.renren.com/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
req = Request(url,headers=headers)
res = urlopen(req)
print(res.read().decode('utf-8'))
