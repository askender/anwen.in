# -*- coding:utf-8 -*-
from tornado.options import define, options

define("port", default=9999, help="run on the given port", type=int)
define("host", default="127.0.0.1:3306", help="数据库地址")
define("database", default="anwen.in", help="数据库名称")
define("user", default="root", help="数据库用户名")
define("password", default="26129581diu900121", help="数据库密码")

debug=True    #是否debug
