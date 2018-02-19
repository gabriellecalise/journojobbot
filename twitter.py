import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search, q='#journalismjobs').items():
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

        #sleep limits the tweeting to occur every __ seconds
        sleep(3600)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
