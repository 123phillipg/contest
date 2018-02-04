#Acquire twitter credentials from the text file that isn't stored on github
credentials = open("credentials.txt","r")
CONSUMER_KEY = credentials.readline().rstrip()
CONSUMER_SECRET = credentials.readline().rstrip()
ACCESS_TOKEN = credentials.readline().rstrip()
ACCESS_TOKEN_SECRET = credentials.readline().rstrip()

import tweepy

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

search_results = api.search(q = "RT to win", count = 100)

for tweet in search_results:
    print tweet.text
