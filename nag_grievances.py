#!/usr/bin/env python3

import tweepy
from settings import *

#This file will post a nag to troll for more grievances


# Try to connect to Twitter first
try:
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
except:
	print("Error Connecting to Twitter")
	exit

try:
	api.update_status('Air your grievances! http://lisgrievances.com for details')
	print("Done")

except:
	print("Could not nag")
	pass

