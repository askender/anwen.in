# -*- coding:utf-8 -*-

db = {
    'type': 'sqlite',  # sqlite or mysql
    'name': 'anwen-test',  # anwentest.db
    'user': 'root',
    'passwd': ''
}

try:
    from db_config_server import *
except:
    pass
