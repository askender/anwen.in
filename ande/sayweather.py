# -*- coding:utf-8 -*-

# import google_weather


def sayweather(usersay, city):
    sayweather = ''
    if u'天气' in usersay:
        my_weather = google_weather.weather(city)
        sayweather += my_weather.get_courent_weather_string()
        sayweather += my_weather.get_forecast_weather_string()
    return sayweather
