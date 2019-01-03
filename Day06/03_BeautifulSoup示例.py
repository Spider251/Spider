from bs4 import BeautifulSoup

html = '''
<div class="text">天霸动霸Tua</div>
<div class="text">杨幂</div>
<div class="text2">
    <span>胡歌</span>
</div>
'''
# 创建解析对象
soup = BeautifulSoup(html,'lxml')
# 调用find_all()方法
rList = soup.find_all('div',attrs = {"class":"text2"})
print(rList)
for r in rList:
    # string属性只能获取当前节点内的文本内容
    print(r.span.string)
    #get_text()能获取当前节点所有文本内容,包括子节点的文本内容
    print(r.get_text())
    print(r.text)
    