import re

html = """
<div><p>你妹真的是你妹</p></div>
<div><p>床前明月光</p></div>
"""

# 创建编译对象
p = re.compile(r'<div><p>(.*?)</p></div>',re.S)
r = p.findall(html)
print(r)