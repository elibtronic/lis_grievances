#!/usr/bin/env python

import tweepy
import urllib, urllib2
from settings import *

#This will check for DMs sent to the bot, post them to Google form
#send a response and delete the DM

try:
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
	dms = api.direct_messages()

	for m in dms:
		mres = api.send_direct_message(m.sender.screen_name, text="Thanks, your grievance has been queued for approval.")
		
		#Grievances are tabulated annoymously in a Google Form where they are eventually posted
		#This part of the process will be automated in future version
		req = urllib2.Request(GFORM_URL+urllib.quote(m.text))
		res = urllib2.urlopen(req)

		#Destroy the message received and the response to it
		api.destroy_direct_message(m.id)
		api.destroy_direct_message(mres.id)
	print "Done"

except:
	print "Could not connect to Twitter"
