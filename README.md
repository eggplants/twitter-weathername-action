# twitter-weathername-action

- Update Twitter's Username to today forecast of given location with GitHub Actions

# Require

- [Openweathermap API Token](https://openweathermap.org/appid)
  - `OPEN_WEATHER_API_TOKEN`
- [Location query](https://openweathermap.org/current#name)
  - `LOCATION_QUERY`
  - City name, state code and country code divided by comma, use ISO 3166 country codes.
- [Twittter API Token](https://developer.twitter.com/en/docs/twitter-api/getting-started/guide)
  - `TWITTER_CONSUMER_KEY`
  - `TWITTER_CONSUMER_SECRET`
  - `TWITTER_ACCESS_KEY`
  - `TWITTER_ACCESS_SECRET`

## On GitHub Actions

- Fork or import this repo
- Set each required parameters to it from `[Settings] Tab ->[Secrets] Tab`
- If that is correct, your Twitter Username will be changed on 00:00

## On local

- Edit `.env.example`
- Rename to `.env`
- Run: `python weather_name.py`
