#Acquire twitter credentials from the text file that isn't stored on github
credentials = open("credentials.txt","r")
consumerKey = credentials.readline().rstrip()
consumerSecret = credentials.readline().rstrip()
accessToken = credentials.readline().rstrip()
accessTokenSecret = credentials.readline().rstrip()

import tweepy

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)


