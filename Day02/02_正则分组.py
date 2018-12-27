import re
#s = "A B C D"
#p1 = re.compile('\w+\s+\w+')
#print(p1.findall(s))
#
#p2 = re.compile('(\w+)\s+\w+')
#print(p2.findall(s))
#
#p3 = re.compile('(\w+)\s+(\w+)')
#print(p3.findall(s)) 


html = '''<div class="animal">
                <p class="name">
                    <a title="Tiger">
                    </a>
                </p>
                <p class="content">
                    Two tigers two tigers run fast
                </p>
            </div>
            <div class="animal">
                <p class="name">
                    <a title="Rabbit">
                    </a>
                </p>
                <p class="content">
                    Small white rabbit white and white
                </p>
            </div>
            '''
p = re.compile('<a title="(.*?)">.*?<p class="content">(.*?)</p>',re.S)
text = p.findall(html)
#print(text)
#for i in range(len(text)):
#    name = text[i][0]
#    describe = text[i][1].split('\n')[1].strip()
#    print("动物名称:",name)
#    print("动物描述:",describe)
#    print("******************")

for r in text:
    name = r[0].strip()
    describe = r[1].strip()
    print(name)
    print(describe)