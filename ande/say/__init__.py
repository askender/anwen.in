# -*- coding:utf-8 -*-

import random


def firstmeet():
    firsthello_list = ['Hello', 'Hi']
    firsthello = random.choice(firsthello_list)
    return firsthello


def expression():
    normal = ['~', '~~~']
    normal = random.choice(normal)
    return normal


def hello(usersay):
    sayhello = ''
    if u'你好' in usersay:
        sayhello += u'你也好'
    return sayhello


def song(usersay):
    saysong = ''
    if u'播放' in usersay:
        saysong += u'好的~'
        song = usersay.split(u'播放')[1]
        songbox = 'http://box.baidu.com/widget/flash/song.swf?name='
        songbox += song + '&autoPlay=true'
        saysong += '<embed  width="500" height="75" src='
        saysong += songbox + 'type="application/x-shockwave-flash"/>'
    return saysong
