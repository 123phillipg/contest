#Acquire twitter credentials from the text file that isn't stored on github
credentials = open("credentials.txt","r")
consumerKey = credentials.readline()
consumerSecret = credentials.readline()
accessToken = credentials.readline()
accessTokenSecret = credentials.readline()


import twitter
api = twitter.Api(consumer_key = "\'"+consumerKey+"\'", consumer_secret = "\'" + consumerSecret + "\'", access_token_key = "\'" + accessToken + "\'", access_token_secret = "\'" + accessTokenSecret + "\'")
