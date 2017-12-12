#!/usr/bin/env python
# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET

#创建根节点
new_xml = ET.Element("namelist")
#在根节点下创建子节点name
name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
#在子节点name下创建子节点age
age = ET.SubElement(name, "age", attrib={"checked": "no"})
#在子节点name下创建子节点sex
sex = ET.SubElement(name, "sex")
#给sex赋值
sex.text = '33'

# #在根节点下创建子节点name2
# name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
# #在子节点name2下创建子节点age
# age = ET.SubElement(name2, "age")
# #给age赋值
# age.text = '19'

## 生成文档对象
et = ET.ElementTree(new_xml)
et.write("namelist.xml", encoding="utf-8", xml_declaration=True)#xml_declaration=True头部声明

ET.dump(new_xml)  # 打印生成的格式【给自己看；可以不写】
