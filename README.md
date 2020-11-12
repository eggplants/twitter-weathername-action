# twitter-weathername-action

[![Test](https://github.com/eggplants/twitter-weathername-action/workflows/Test/badge.svg)](https://github.com/eggplants/twitter-weathername-action/actions/runs/359325081)

![demo](https://i.imgur.com/Mv8T1mV.png)

- Update Twitter's Username to today forecast of given location with GitHub Actions

## Parameters

### Required

- `OPEN_WEATHER_API_TOKEN`
  - [Openweathermap API Token](https://openweathermap.org/appid)
- `LOCATION_QUERY`
  - [Location query](https://openweathermap.org/current#name)
  - City name, state code and country code divided by comma, use ISO 3166 country codes
- `TWITTER_CONSUMER_KEY`
- `TWITTER_CONSUMER_SECRET`
- `TWITTER_ACCESS_KEY`
- `TWITTER_ACCESS_SECRET`
  - [Twitter API Token](https://developer.twitter.com/en/docs/twitter-api/getting-started/guide)

### Optional

- `TIME_ZONE`
  - Def: LOCATION_QUERY's local time zone
  - Time zone to be used as a time reference
  - Ex. `Asia/Tokyo`
- `NAME_FORMAT`
  - Def: `＜{}`
  - Username format
  - `{}` is substituted by joined weather icons with `ICON_SEP`
- `ICON_SEP`
  - Def: `:`
  - String for joining icons
- `FORECAST_DAY`
  - Def: `0`
  - Show the weather in the next given (0~4) days
  - `0` is today

## Example

- [cron_renamer.yml](https://github.com/eggplants/twitter-weathername-action/blob/main/.github/workflows/cron_renamer.yml)

```yml
name: Cron renamer

on:
  schedule:
    - cron: "0 0 * * *"

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Change Name
        uses: eggplants/twitter-weathername-action@v2
        with:
          open_weather_api_token: ${{ secrets.OPEN_WEATHER_API_TOKEN }}
          twitter_consumer_key: ${{ secrets.TWITTER_CONSUMER_KEY }}
          twitter_consumer_secret: ${{ secrets.TWITTER_CONSUMER_SECRET }}
          twitter_access_key: ${{ secrets.TWITTER_ACCESS_KEY }}
          twitter_access_secret: ${{ secrets.TWITTER_ACCESS_SECRET }}
          location_query: tsukuba
          name_format: "明日: {}"
          icon_sep: "/"
          forecast_day: 1
```
