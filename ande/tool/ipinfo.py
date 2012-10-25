#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import json


def ipinfo():
    ipinfo = urllib.urlopen(
        'http://int.dpool.sina.com.cn/iplookup/\
        iplookup.php?format=json').read()
    ipinforeal = json.loads(ipinfo)
    country = ipinforeal['country']
    #http://int.dpool.sina.com.cn/iplookup/iplookup.php
    # ?format=json&ip=115.156.238.114
    return country


def main():
    print ipinfo()

if __name__ == '__main__':
    main()
