# twitter-weathername-action

![demo](https://i.imgur.com/Mv8T1mV.png)

- Update Twitter's Username to today forecast of given location with GitHub Actions

## Require

- [Openweathermap API Token](https://openweathermap.org/appid)
  - `OPEN_WEATHER_API_TOKEN`
- [Location query](https://openweathermap.org/current#name)
  - `LOCATION_QUERY (def: "tsukuba")`
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

    OPTIONAL:
        LOCATION_QUERY
        NAME_FORMAT
        ICON_SEP
}
```
