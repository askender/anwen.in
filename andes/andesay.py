# -*- coding:utf-8 -*-

import string
import urllib2
import json

import fenci
from xpinyin import Pinyin
from sayhello import *
from sayweather import *
from saysong import *


class AndeSay(object):
    """ande 的反馈

    usage
    -----
    ::
        In [1]: from andesay import AndeSay
        In [2]: a = AndeSay()
        In [3]: p.get_andesay(u"你好")
        Out[3]: ''
        In [4]: p.get_andethink(u"你")
        Out[4]: ''
    请输入utf8编码汉字

    .. ande_ai: https://github.com/askender/ande_ai not open
    """

    def __init__(self):
        city_info=urllib2.urlopen( 'http://pv.sohu.com/cityjson').read().decode('GBK')
        self.ip = city_info.split('=')[1].split(',')[0].split('"')[3] #取出地址信息.encode("utf-8")
        self.zipcode = city_info.split('=')[1].split(',')[1].split('"')[3] #取出地址信息
        self.addr = city_info.split('=')[1].split(',')[2].split('"')[3] #取出地址信息
        self.provice = self.addr.split(u'省',1)[0].replace(' ','') #获取省份
        # self.city = ''
        # if u'市' in self.addr:
        #     self.city = self.addr.split(u'市')[0].split(u'省')[1].strip().replace(' ','') #获取城市

    def is_cn_char(self,i):
        return 0x4e00<=ord(i)<0x9fa6

    def is_cn_or_en(self,i):
        o = ord(i)
        return o<128 or 0x4e00<=o<0x9fa6

    def is_cn(self,i):
        is_cn = 'is_cn'
        c = i.encode('utf-8')
        if len(c) == len(i):
            is_cn = 'not_cn'
        return is_cn

    def is_ascii(self,i):
        is_ascii = 'is_ascii'
        for c in i:
            if c not in string.ascii_letters:
                is_ascii = 'not_ascii'
                return is_ascii
        return is_ascii

    def get_ip(self):
        get_ip = self.ip
        return get_ip


    def get_andesay(self, usersay, splitter=''):
        andesay = ''

        p = Pinyin()
        userfenci = fenci.fenci(usersay)
        userfencij = json.loads(userfenci)
        is_cn = self.is_cn(usersay)
        #city = p.get_pinyin(self.city)

        #andesay += sayweather(usersay,city)
        andesay += sayhello(usersay)
        andesay += saysong(usersay)

        debug = True
        if debug:
            andesay += '<br/>ande-think-trace,it will remove'
            andesay += '<br/>'+self.is_cn(usersay)
            andesay += '<br/>'+self.is_ascii(usersay)
            andesay += '<br/>'+userfenci
            andesay += '<br/>'+p.get_pinyin(usersay)
            andesay += '<br/>'+self.ip+'<br/>'+self.zipcode+'<br/>'
            andesay += '<br/>'+self.addr
            andesay += '<br/>'+self.provice#+'<br/>'+self.city
        #status = userfenci['words'][0]['attr']
        #status += userfenci['words'][1]['attr']
        return andesay