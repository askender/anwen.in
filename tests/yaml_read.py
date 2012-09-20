 # -*- coding: utf-8 -*- 
import yaml
#读取yaml文件

stream = file('document.yaml', 'r')    
dict =  yaml.load(stream)
print dict
#打印所有的yaml数据，其实也就是dict类，《简明_python_教程》里说的字典
print dict["name"]
#打印其中的一个key值
