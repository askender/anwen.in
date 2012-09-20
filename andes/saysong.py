# -*- coding:utf-8 -*-

def saysong(usersay):
    saysong = ''
    if u'播放' in usersay:
        saysong += u'好的~'
        song = usersay.split(u'播放')[1]
        songbox = 'http://box.baidu.com/widget/flash/song.swf?name='+song+'&autoPlay=true';
        saysong += '<embed  width="500" height="75" src='+songbox+'type="application/x-shockwave-flash"/>';
    return saysong