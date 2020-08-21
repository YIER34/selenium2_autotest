# 读取xml文件
# 适用于读取不规则文件，例如配置文件的url/浏览器/登录的用户名和密码

from xml.dom import minidom
# 打开xml文档
dom = minidom.parse('info.xml')
# 得到文档元素对象(得到xml文件的唯一根元素)
root = dom.documentElement

'''
# 1. 获取标签信息
# 每一个节点都有它的nodeName(节点名称)，nodeValue(节点的值,只对文本节点有效)，nodeType(节点类型)
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)
'''
'''
# 2. 获得任意标签名,getElementsByTagName()通过标签名获取标签，标签名有多个时，通过下标获取
tagname = root.getElementsByTagName('browser')
print(tagname[0].tagName)
tagname = root.getElementsByTagName('login')
print(tagname[1].tagName)
tagname = root.getElementsByTagName('province')
print(tagname[2].tagName)
'''

# 3. 获取标签的属性值
logins = root.getElementsByTagName('login')
# 获取login标签的username属性

username = logins[0].getAttribute("username")
print(username)

# 获取login标签的password属性
password = logins[0].getAttribute("password")
print(password)

# 获取第二个login标签的属性值
username = logins[1].getAttribute("username")
print(username)
password = logins[1].getAttribute("password")
print(password)

# 4. 获取标签对之间的数据

provinces = root.getElementsByTagName('province')
citys = root.getElementsByTagName('city')

#获取第一个provinces标签对的值
# firstChild属性返回被选节点的第一个子节点；data表示获取该节点的数据，与webdriver的text方法类似
p1 = provinces[0].firstChild.data
print(p1)

#获取第一个city标签对的值
c1 = citys[0].firstChild.data
print(c1)
#获取第二个city标签对的值
c2 = citys[1].firstChild.data
print(c2)

