#Twitter web service

import tweepy

consumer_key = "<get your own>"
consumer_secret = "<get your own>"
access_token = "<get your own>"
access_secret = "<get your own>"

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

tweets = api.search(q='#python')

#disply results to screen
for t in tweets:
	print t.created_at, t.text, "\n"