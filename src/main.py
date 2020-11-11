from os import environ
from os.path import dirname, join

import dotenv

from weathername import GetTodayWeather, UpdateName

dotenv_path = join(dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)


def main() -> None:
    g = GetTodayWeather()
    w = g.today_weathers()
    today_weather_icons = g.weather_icons(w)
    name_format = environ.get('NAME_FORMAT', '＜{}')
    icon_sep = environ.get('ICON_SEP', ':')
    name = name_format.format(icon_sep.join(today_weather_icons))
    UpdateName().update(name)


if __name__ == '__main__':
    main()
