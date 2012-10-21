#--coding:utf-8--

import urllib2
from xml.dom import minidom


class weather:
    def __init__(self,location):
        #从google获得ｘｍｌ格式的天气信息
        #返回的ｘｍｌ是gb2312的，字符串初始为ａｃｃｉｉ编码，使用gb2312编码转成unicode,再转为utf-8
        try:
            xml = urllib2.urlopen('http://www.google.com/ig/api?hl=zh-cn&weather=%s' % (location)).read().decode('gb2312').encode('utf-8')
        except ValueError:
            print "Could not convert data to an integer."
            #raise u'不好，在获取google天气信息时遇到错误！'
        else:
            try:
                #使用ｍｉｎｉｄｏｍ初始化ｘｍｌ
                root = minidom.parseString(xml).documentElement
            except:
                raise u'初始化xml是遇到错误，xml传输错误，或者google给的xml格式不标准'
            else:
                self.root = root
                self.weather_data= {}
                self.weather_data['today'] = {}
                self.weather_data['forecast'] = []


    def get_courent_weather(self):
        dom = self.root.getElementsByTagName('current_conditions')[0]
        self.weather_data['today']['condition'] = dom.getElementsByTagName('condition')[0].attributes['data'].value
        self.weather_data['today']['temp_c'] = dom.getElementsByTagName('temp_c')[0].attributes['data'].value
        self.weather_data['today']['humidity'] = dom.getElementsByTagName('humidity')[0].attributes['data'].value
        self.weather_data['today']['wind_condition'] = dom.getElementsByTagName('wind_condition')[0].attributes['data'].value
        return self.weather_data['today'] #返回当前天气状况的一个字典

    def get_courent_weather_string(self):
        today_weather = self.get_courent_weather()
        today_weather_string = u'今天天气:\n' + today_weather['condition'] + '\n'\
                               + u'当前温度' + today_weather['temp_c']  + '\n'\
                               + u'当前湿度' + today_weather['humidity']  + '\n'\
                               + u'当前风速' + today_weather['wind_condition'] + '\n'
        return today_weather_string

    def get_forecast_weather(self):
        doms = self.root.getElementsByTagName('forecast_conditions')
        self.weather_data['forecast'] = []
        for dom in doms:
            bufdict = {} #未来每天数据的ｂｕｆｆｅｒ
            bufdict['day_of_week'] = dom.getElementsByTagName('day_of_week')[0].attributes['data'].value
            bufdict['low'] = dom.getElementsByTagName('low')[0].attributes['data'].value
            bufdict['high']= dom.getElementsByTagName('high')[0].attributes['data'].value
            bufdict['condition']= dom.getElementsByTagName('condition')[0].attributes['data'].value
            self.weather_data['forecast'].append(bufdict)
        return self.weather_data['forecast'] #返回未来4天的天气的一个列表，元素ｗｅｉ字典
    def get_forecast_weather_string(self):
        forecast_weather = self.get_forecast_weather()
        forecast_weather_string = ''
        for i in forecast_weather:
            forecast_weather_string += i['day_of_week'] + '\n' \
                                       + u'最低温度:' + i['low'] + '\n' \
                                       + u'最高温度:' + i['high'] + '\n' \
                                       + u'天气状况:' + i['condition'] + '\n'
        return forecast_weather_string


    def get_data(self):
        self.get_courent_weather()
        self.get_forecast_weather()
        return self.weather_data
    def get_data_string(self):
        return self.get_courent_weather_string() + self.get_forecast_weather_string()

if __name__ == '__main__':
    my_weather = weather('heze')
    print my_weather.get_courent_weather_string()
    print my_weather.get_forecast_weather_string()
