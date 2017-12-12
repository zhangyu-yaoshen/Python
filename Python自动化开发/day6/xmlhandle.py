#!/usr/bin/env python
# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET

#打开并解析文件
tree = ET.parse("xmltest.xml")#parse解析
root = tree.getroot()
print(root.tag)#打印xml文件的根

# # 循环xml文件
# for child in root:
#     print(child.tag, child.attrib)
#     for i in child:
#         print(i.tag, i.text,i.attrib)
# #tag=year;text=2008;attrib={}

# # 只循环country节点
# for node in root.iter('country'):
#     print(node.tag, node.text, node.attrib)

# # 修改【年的加1】
# for node in root.iter('year'):
#     new_year = int(node.text) + 1#年加1
#     node.text = str(new_year)#用新的替换老的
#     node.set("updated", "yes")#加入属性
# tree.write("xmltest2.xml")#写入新的文件【可以写入源文件】

# 删除node
for country in root.findall('country'):#找到country
    rank = int(country.find('rank').text)#找到country里rank字段
    if rank > 50:#判断是否大于50
        root.remove(country)#删除此country
tree.write('output.xml',encoding="utf-8")#写入新的文件【可以写入源文件】

















