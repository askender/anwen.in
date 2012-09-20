 # -*- coding: utf-8 -*- 
import yaml
#生成yaml文件
document = """
name: Vorlin Laruknuzum
sex: Male
class: Priest
title: Acolyte
hp: [32, 71]
sp: [1, 13]
gold: 423
inventory:
- a Holy Book of Prayers (Words of Wisdom)
- an Azure Potion of Cure Light Wounds
- a Silver Wand of Wonder
"""
print  yaml.dump(yaml.load(document))
#打印由字符转换成python对象的yaml格式信息
stream = file('document.yaml', 'w')
yaml.dump(yaml.load(document), stream)
#写文件    # Write a YAML representation of data to 'document.yaml'.
print yaml.dump(yaml.load(document))  