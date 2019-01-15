import tweepy
from time import sleep

from tweepy import TweepError

auth = tweepy.OAuthHandler(consumer_key='', consumer_secret='')
auth.set_access_token(key='', secret='')

api = tweepy.API(auth)
ID = ''
lastID = ''
while True:
    responseArray = api.user_timeline(id=ID) if not lastID else api.user_timeline(id=ID, since_id=lastID)
    first = True
    for k in responseArray:
        try:
            api.create_favorite(id=k.id)
            print(f'Liked Tweet {k.id}')
        except TweepError:
            print(f'Tweet {k.id} was already liked!')
        finally:
            if first:
                lastID = k.id
                first = False
    sleep(10)
