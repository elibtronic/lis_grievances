#!/usr/bin/env python

import tweepy
import urllib, urllib2
from settings import *

# Insurance policy, running this will delete DMs the bot has

try:
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
	dms = api.direct_messages()
	# The nuclear option, will delete all DM's to the bot.
	for m in dms:
		api.destroy_direct_message(m.id)
	print "Done"
except:
	print "Could not connect to twitter"
