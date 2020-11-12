from os import environ
from sys import stderr

import tweepy  # type: ignore


class UpdateName(object):

    def __init__(self) -> None:
        self.api = self.__auth()

    def __auth(self):
        try:
            auth = tweepy.OAuthHandler(environ.get('INPUT_TWITTER_CONSUMER_KEY'),
                                       environ.get('INPUT_TWITTER_CONSUMER_SECRET'))
            auth.set_access_token(environ.get('INPUT_TWITTER_ACCESS_KEY'),
                                  environ.get('INPUT_TWITTER_ACCESS_SECRET'))
            auth.secure = True
            api = tweepy.API(auth)
        except tweepy.TweepError as e:
            print(e, file=stderr)
            exit(1)

        return api

    def update(self, name: str) -> None:
        self.api.update_profile(name)
