# -*- coding:utf-8 -*-

import random
import json
import urllib


def firstmeet():
    firsthello_list = ['Hello', 'Hi']
    firsthello = random.choice(firsthello_list)
    return firsthello


def expression():
    normal = ['~', '~~~']
    normal = random.choice(normal)
    return normal


def hello(usersay):
    hello = ''
    if u'你好' in usersay:
        hello += u'你也好'
    return hello


def song(usersay):
    song = '<br />'
    if u'播放' in usersay:
        song += u'好的~'
        artist = ''
        songname = usersay.split(u'播放')[1]
        if '@@' in songname:
            artist = songname.split('@@')[1]
            songname = songname.split('@@')[0]
        songname = urllib.quote(songname.encode('utf-8'))
        songbox = '<p><embed width="500" height="75" name="plugin" src="http://box.baidu.com/widget/flash/song.swf?name='
        songbox += songname
        if artist:
            songbox += '&amp;artist=' + artist
        songbox += '" type="application/x-shockwave-flash"></p>'
        song += songbox
    print song
    return song


def get_ande_ip():
    return urllib.urlopen('http://ifconfig.me/ip').read()


def get_ipinfo(ip):
    if ip == '127.0.0.1':
        ip = get_ande_ip()
    return json.loads(urllib.urlopen(
        'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip).read())


def get_weather(city):
    url = 'http://sou.qq.com/online/get_weather.php?callback=Weather&city='
    city = urllib.quote(city.encode('utf-8'))
    return json.loads(urllib.urlopen(url + city).read()[8:-2])


def weather(usersay, userip):
    weather = ''
    if u'天气' in usersay:
        city = get_ipinfo(userip)['data']['city']
        weather = get_weather(city)
        wea_0 = weather['future']['wea_0']
        tmin_0 = weather['future']['tmin_0']
        tmax_0 = weather['future']['tmax_0']
        weather = u'今天天气是%s,%s到%s是摄氏度' % (wea_0, tmin_0, tmax_0)
    return weather
