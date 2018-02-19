import tweepy

#variables for keys and such
consumer_key = 'GI2EEOOIQHyAcBC9ntc8o62YC'
consumer_secret = 'aFbAh00MYDe80Ji8eR0rOPNHKJuqvdk4bj5YHsg0oMlUydyWZn'
access_token = '963468858798608384-0xoosT6hSOWto530pasilYqTBq2kPWX'
access_token_secret = 'TgqWeifQtR0LUAlu8FPHIQAuxuOFyQ0b4kaADLm003HIZ'

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Write a tweet to push to our Twitter account
tweet = 'Want a #journojob? Check out JournoJobBot for updates on new postings!'
api.update_status(status=tweet)
