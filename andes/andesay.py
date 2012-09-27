# -*- coding:utf-8 -*-

import string
import urllib
import urllib2
import json

from tool.fenci import fenci
from tool.xpinyin import Pinyin
from sayhello import sayhello
from sayweather import sayweather
from saysong import saysong


class AndeSay(object):


    def __init__(self):
        city_info=urllib2.urlopen( 'http://pv.sohu.com/cityjson').read().decode('GBK')
        self.ip = city_info.split('=')[1].split(',')[0].split('"')[3] #取出地址信息.encode("utf-8")
        self.zipcode = city_info.split('=')[1].split(',')[1].split('"')[3] #取出地址信息
        self.addr = city_info.split('=')[1].split(',')[2].split('"')[3] #取出地址信息
        self.provice = self.addr.split(u'省',1)[0].replace(' ','') #获取省份
        # self.city = ''
        # if u'市' in self.addr:
        #     self.city = self.addr.split(u'市')[0].split(u'省')[1].strip().replace(' ','') #获取城市


    def user_ip(self):
        user_ip = urllib.urlopen('http://ifconfig.me/ip').read()
        return user_ip

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


    def get_andesay(self, usersay, splitter=''):
        andesay = ''

        p = Pinyin()
        userfenci = fenci(usersay)
        userfencij = json.loads(userfenci)
        is_cn = self.is_cn(usersay)
        #city = p.get_pinyin(self.city)

        #andesay += sayweather(usersay,city)
        andesay += sayhello(usersay)
        andesay += saysong(usersay)

        andethink = ''
        andethink += '<br/>ande-think-trace,it will remove'
        andethink += '<br/>'+self.user_ip()
        andethink += '<br/>'+self.is_cn(usersay)
        andethink += '<br/>'+self.is_ascii(usersay)
        andethink += '<br/>'+userfenci
        andethink += '<br/>'+p.get_pinyin(usersay)
        andethink += '<br/>'+self.ip+'<br/>'+self.zipcode+'<br/>'
        andethink += '<br/>'+self.addr
        andethink += '<br/>'+self.provice#+'<br/>'+self.city
        #status = userfenci['words'][0]['attr']
        #status += userfenci['words'][1]['attr']

        debug = True # True False
        if debug:
            andesay += andethink

        return andesay