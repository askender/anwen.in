# -*- coding:utf-8 -*-

import string
import urllib

from tool.fenci import fenci
from tool.xpinyin import Pinyin
import say


class AndeSay(object):

    def is_cn_char(self, i):
        return 0x4e00 <= ord(i) < 0x9fa6

    def is_cn_or_en(self, i):
        o = ord(i)
        return o < 128 or 0x4e00 <= o < 0x9fa6

    def is_cn(self, i):
        is_cn = 'is_cn'
        c = i.encode('utf-8')
        if len(c) == len(i):
            is_cn = 'not_cn'
        return is_cn

    def is_ascii(self, i):
        is_ascii = 'is_ascii'
        for c in i:
            if c not in string.ascii_letters:
                is_ascii = 'not_ascii'
                return is_ascii
        return is_ascii

    def ande_ip(self):
        return urllib.urlopen('http://ifconfig.me/ip').read()

    def get_andesay(self, usersay, splitter=''):
        andesay = ''
        andesay += '<br/>'
        p = Pinyin()
        userfenci = fenci(usersay)
        # userfencij = json.loads(userfenci)
        # is_cn = self.is_cn(usersay)
        # city = p.get_pinyin(self.city)

        # andesay += sayweather(usersay,city)
        andesay += say.hello(usersay)
        andesay += say.song(usersay)

        andethink = ''
        andethink += '<br/>ande-think-trace, just for study'
        andethink += '<br/>ande ip:' + self.ande_ip()
        andethink += '<br/>' + self.is_cn(usersay)
        andethink += '<br/>' + self.is_ascii(usersay)
        andethink += '<br/>' + userfenci
        andethink += '<br/>' + p.get_pinyin(usersay)
        #status = userfenci['words'][0]['attr']

        debug = True  # True False
        if debug:
            andesay += andethink

        return andesay
