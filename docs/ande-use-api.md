安德使用的接口 ande-use-api
========

ip
- self.request.remote_ip
- http://ifconfig.me/ip
- http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json wrong
- http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip= no_use

weather
- 
http://m.weather.com.cn/data/101110101.html 六天预报
http://www.weather.com.cn/data/sk/101110101.html 实时天气信息
http://www.weather.com.cn/static/html/legend.shtml 天气图例
XML接口 http://flash.weather.com.cn/wmaps/xml/china.xml 这个是全国天气的根节点，列出所有的省，其中的pyName字段是各个省XML的文件名
北京的XML地址为 http://flash.weather.com.cn/wmaps/xml/beijing.xml
http://m.weather.com.cn/img/c0.gif http://m.weather.com.cn/img/b0.gif http://www.weather.com.cn/m/i/weatherpic/29x20/d0.gif http://www.weather.com.cn/m2/i/icon_weather/29x20/n00.gif 这个图就是天气现象0（晴）的图片，其他天气现象的图片依此类推。c打头的图片是20*20像素的，b打头的是50*46像素的，d打头的是反白的图标，29*20像素，n打头的是夜间反白图标，29*20像素
http://flash.weather.com.cn/sk2/101220607.xml
http://flash.weather.com.cn/sk2/shikuang.swf?id=101220607
http://www.weather.com.cn/static/custom/search3.htm
备用：
http://www.weather.com.cn/html/weather/101010200.shtml
http://sou.qq.com/online/get_weather.php?callback=Weather&city=武汉
http://tianqi.2345.com/t/
http://tianqi.2345.com/t/detect2009v2.php
http://www.hujuntao.com/api/weather/api.php?city=武汉
http://toy.weather.com.cn/SearchBox/searchBox?callback=jsonp1343396048201&_=1343396067262&language=zh&keyword=武汉
http://www.youdao.com/smartresult-xml/search.s?type=weather&jsFlag=true&q=南京