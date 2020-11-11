import json
import os
import sys
from datetime import datetime as d
from datetime import timedelta
from os.path import dirname, join
from typing import List, Optional

import dotenv
import requests
import tweepy

dotenv_path = join(dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)
ENV = os.environ

'''
ENV{
    OPEN_WEATHER_API_TOKEN
    TWITTER_CONSUMER_KEY
    TWITTER_CONSUMER_SECRET
    TWITTER_ACCESS_KEY
    TWITTER_ACCESS_SECRET
    LOCATION_QUERY
}
'''


class GetTodayWeather(object):
    def __init__(self) -> None:

        self.weather_info = json.loads(open('sampledata.json', 'r').read())
        self.timezone = self.weather_info['city']['timezone']

    def get_weather(self):
        url = 'http://api.openweathermap.org/data/2.5/forecast?'\
              'q={0}&lang=ja&appid={1}'
        res = requests.get(url.format(
            ENV['LOCATION_QUERY'],
            ENV['OPEN_WEATHER_API_TOKEN']
        ))
        res = res.json()
        # print(type(res))
        # exit()
        # validate
        if 'city' not in res:
            print('invalid json was returned:', res, file=sys.stderr)
            exit(1)

        self.weather_info, self.timezone = res, res['city']['timezone']
        return res

    def today_weathers(self):
        def filter_day(day, dt):
            return day <= d.fromtimestamp(dt) < day + timedelta(days=1)

        t = d.today()
        weather_datas = self.weather_info['list']
        today_weathers = [_ for _ in weather_datas if filter_day(t, _['dt'])]
        return today_weathers

    def weather_icons(self, weather_data):
        icons = [self.__convert_icon(str(weather['weather'][0]['id']))
                 for weather in weather_data]
        return icons

    def __convert_icon(self, weather_id: str) -> str:

        # modified: https://gist.github.com/michels/90327b8d284646a238e6
        default = '🌀'

        if not weather_id:
            return default

        car = self.__judge_car(weather_id[0])
        cdr = self.__judge_id(weather_id)
        if car:
            return car
        elif cdr:
            return cdr
        else:
            return default

    def __judge_car(self, car):
        thunderstorm = '⚡'    # Code: 200's
        drizzle = '🌧️'         # Code: 300's
        rain = '☔'            # Code: 500's
        snowflake = '❄'       # Code: 600's snowflake
        snowman = '⛄'         # Code: 600's snowman
        atmosphere = '🌫'  # Code: 700's foogy

        if car == '2':
            return thunderstorm
        elif car == '3':
            return drizzle
        elif car == '5':
            return rain
        elif car == '6':
            return snowflake + snowman
        elif car == '7':
            return atmosphere
        else:
            return None

    def __judge_id(self, id_: str) -> Optional[str]:
        clearSky = '☀'        # Code: 800 clear sky
        fewClouds = '⛅'       # Code: 801 sun behind clouds
        clouds = '☁'  # Code: 802-803-804 clouds general

        if id_ == '800':
            return clearSky
        elif id_ == '801':
            return fewClouds
        elif id_ in ['802', '803', '804']:
            return clouds
        else:
            return None


class UpdateName(object):
    def __init__(self):
        self.api = self.__auth()

    def __auth(self):
        auth = tweepy.OAuthHandler(ENV['TWITTER_CONSUMER_KEY'],
                                   ENV['TWITTER_CONSUMER_SECRET']
                                   )
        auth.set_access_token(ENV['TWITTER_ACCESS_KEY'],
                              ENV['TWITTER_ACCESS_SECRET'])
        auth.secure = True
        api = tweepy.API(auth)
        return api

    def update(self, name: str) -> None:
        self.api.update_profile(name)


def main():
    g = GetTodayWeather()
    w = g.today_weathers()
    UpdateName().update('{}'.format(":".join(g.weather_icons(w))))


if __name__ == '__main__':
    main()
