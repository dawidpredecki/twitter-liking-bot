import tweepy
import time

auth = tweepy.OAuth1UserHandler('CONSUMER_KEY', 'CONSUMER_SECRET', 'ACCESS_TOKEN', 'ACCESS_TOKEN_SECRET')

api = tweepy.API(auth, wait_on_rate_limit=True)

search = input('Keyword: ')
number_of_tweets = 1000

for tweet in tweepy.Cursor(api.search_tweets, search).items(number_of_tweets):
    try:
        print('Tweet Liked!')
        tweet.favorite()
        time.sleep(5)
    except tweepy.TweepyException as e:
        print(e)
    except StopIteration:
        break
