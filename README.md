# twitter-weathername-action

![demo](https://i.imgur.com/Mv8T1mV.png)

- Update Twitter's Username to today forecast of given location with GitHub Actions

## Require

- [Openweathermap API Token](https://openweathermap.org/appid)
  - `OPEN_WEATHER_API_TOKEN`
  - `TIME_ZONE (def: LOCATION_QUERY's local time zone)`
- [Location query](https://openweathermap.org/current#name)
  - `LOCATION_QUERY`
  - City name, state code and country code divided by comma, use ISO 3166 country codes.
- [Twitter API Token](https://developer.twitter.com/en/docs/twitter-api/getting-started/guide)
  - `TWITTER_CONSUMER_KEY`
  - `TWITTER_CONSUMER_SECRET`
  - `TWITTER_ACCESS_KEY`
  - `TWITTER_ACCESS_SECRET`
- `NAME_FORMAT (def: "＜{}")`
- `ICON_SEP (def: ":")`

```txt
ENV{
    REQUIRED:
        OPEN_WEATHER_API_TOKEN
        TWITTER_CONSUMER_KEY
        TWITTER_CONSUMER_SECRET
        TWITTER_ACCESS_KEY
        TWITTER_ACCESS_SECRET
        LOCATION_QUERY

    OPTIONAL:
        TIME_ZONE
        NAME_FORMAT
        ICON_SEP
}
```

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
        uses: eggplants/twitter-weathername-action@v1
        with:
          OPEN_WEATHER_API_TOKEN: ${{ secrets.OPEN_WEATHER_API_TOKEN }}
          TWITTER_CONSUMER_KEY: ${{ secrets.TWITTER_CONSUMER_KEY }}
          TWITTER_CONSUMER_SECRET: ${{ secrets.TWITTER_CONSUMER_SECRET }}
          TWITTER_ACCESS_KEY: ${{ secrets.TWITTER_ACCESS_SECRET }}
          TWITTER_ACCESS_SECRET: ${{ secrets.TWITTER_ACCESS_SECRET }}
          LOCATION_QUERY: ${{ secrets.LOCATION_QUERY }}
```
