#!/usr/bin/env python
"""
此模块用于初始化用户信息.xml
"""

from xml.etree import ElementTree as ET

root = ET.Element("game-user")
user1 = ET.SubElement(root, "user", attrib={"key": "xmcx"})
name1 = ET.SubElement(user1, "name")
alias1 = ET.SubElement(user1, "alias")
blood1 = ET.SubElement(user1, "blood")
sword1 = ET.SubElement(user1, "sword")
introduct1 = ET.SubElement(user1, "introduce")
kongfu = ET.SubElement(user1,"kongfu")
name1.text = "西门吹雪"
alias1.text = "剑神"
blood1.text = "200"
sword1.text = "乌鞘剑"
kongfu.text = '{"雪染长虹":15, "剑神一笑":30 ,"冰雪交加":20, "雪满天下": 25 }'
introduct1.text = "西门吹雪以剑法超绝立足江湖，生性冷僻，其人不苟言笑，嗜剑如命，取人性命在电光火石之间，视杀人为艺术。" \
                  "长身直立、白衣如雪，腰旁的剑却是黑的，漆黑，狭长，古老，乃天下利器，剑锋三尺七寸，净重七斤十三两"

user2 = ET.SubElement(root, "user", attrib={"key": "ygc"})
name2 = ET.SubElement(user2, "name")
alias2 = ET.SubElement(user2, "alias")
blood2 = ET.SubElement(user2, "blood")
sword2 = ET.SubElement(user2, "sword")
kongfu = ET.SubElement(user2,"kongfu")
introduct2 = ET.SubElement(user2, "introduce")

name2.text = " 叶孤城"
alias2.text = "剑圣"
blood2.text = "200"
sword2.text = "古雅长剑"
kongfu.text = '{"天外飞仙":20, "独孤九剑":30 ,"乾坤一掷":15, "凝神归元": 10 }'
introduct2.text = "其容貌秀丽端庄，自幼痴心向剑，且天资极高，自己悟得上乘剑道，叶孤城自创辉煌至极的剑招「天外飞仙」" \
                  "与燕南天独创强霸无双的剑术「神剑诀」都是傲视天下的剑法，名震海内。配剑乃海外寒鐡精英，吹毛断发，" \
                  "剑锋三尺三，净重六斤四两"

xmlfile = ET.ElementTree(root)
xmlfile.write("users.xml", encoding="utf-8", xml_declaration=True)
