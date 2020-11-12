import sys
from datetime import datetime as d
from datetime import timedelta, timezone
from os import environ
from typing import Any, Dict, List, Optional, Tuple

import requests
from pytz import all_timezones
from pytz import timezone as pytztimezone
from pytz import utc


class GetTodayWeather(object):

    def __init__(self) -> None:
        self.weather_info, self.timezone = self.__get_weather()

    def __valid_timezone_name(self, time_zone: str) -> None:
        if time_zone not in all_timezones:
            raise ValueError(
                'Invalid timezone string!: {}'.format(time_zone))

    def __get_weather(self) -> Tuple[Any, timezone]:
        url = 'http://api.openweathermap.org/data/2.5/forecast?'\
              'q={0}&lang=en&appid={1}'
        res = requests.get(url.format(
            environ.get('INPUT_LOCATION_QUERY'),
            environ.get('INPUT_OPEN_WEATHER_API_TOKEN')
        ))
        res = res.json()
        if 'city' not in res:
            print('invalid json was returned:', res, file=sys.stderr)
            exit(1)

        time_zone = timezone(timedelta(seconds=res['city']['timezone']))
        tz = environ.get('INPUT_TIME_ZONE', '')
        if tz != '':
            self.__valid_timezone_name(tz)
            got_tz = pytztimezone(tz)
            now = d.utcnow()
            now_utc = now.replace(tzinfo=utc)
            now_got = now.astimezone(got_tz)
            gap = now_utc - now_got
            time_zone = timezone(timedelta(seconds=gap.seconds))

        return (res, time_zone)

    def day_weathers(self) -> Dict[str, Any]:
        def _filter(today_dt, dt, count: int) -> bool:
            dt = d.fromtimestamp(dt).astimezone(self.timezone)
            base_dt = today_dt + timedelta(days=count)
            return base_dt <= dt < base_dt + timedelta(days=1)

        today_dt = d.today().astimezone(self.timezone)
        weather_datas = self.weather_info['list']
        day_weathers = {}
        for count in range(7):
            day_weathers[str(count)] = [_ for _ in weather_datas
                                        if _filter(today_dt, _['dt'], count)]
        return day_weathers

    def weather_icons(self, weather_data) -> List[str]:
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

    def __judge_car(self, car: str) -> Optional[str]:
        thunderstorm = '⚡'    # Code: 200's
        drizzle = '🌧️'         # Code: 300's
        rain = '☔'            # Code: 500's
        snowflake = '❄'       # Code: 600's snowflake
        atmosphere = '🌫'      # Code: 700's foogy

        if car == '2':
            return thunderstorm
        elif car == '3':
            return drizzle
        elif car == '5':
            return rain
        elif car == '6':
            return snowflake
        elif car == '7':
            return atmosphere

    def __judge_id(self, id_: str) -> Optional[str]:
        clearSky = '☀'        # Code: 800 clear sky
        fewClouds = '⛅'       # Code: 801 sun behind clouds
        clouds = '☁'          # Code: 802-803-804 clouds general

        if id_ == '800':
            return clearSky
        elif id_ == '801':
            return fewClouds
        elif id_ in ['802', '803', '804']:
            return clouds
