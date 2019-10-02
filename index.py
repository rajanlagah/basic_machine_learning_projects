import tweepy
from textblob import TextBlob

consumer_key = 'xRNZRUDpoeutbVxzT94OFoMbD'
consumer_secret = '8rhtaqmSJ7eZGbMX4NCyIV6PGF2461kXErJJboTD10Kv8zXtYP'

access_token = '1157269866245529602-hBXtoztcOklccw4zT6yY32ytOBkJh5'
access_token_secret = '1BVyCPR7nnbkPa8xwUKglKzbg92r4CXm9xZurkVfS47E4'

auth = tweepy.OAuthHandler(consumer_key , consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#getting data on keyword
public_tweets = api.search('boycottmodia')

# for each tweet printing tweet + sentiment ponits + subjectivity is how much its factual vs opinionated 
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
