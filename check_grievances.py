#!/usr/bin/env python3

import tweepy
import urllib3
from settings import *
from urllib.parse import quote

#This will check for DMs sent to the bot, post them to Google form
#send a response and delete the DM


try:
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
	dms = api.direct_messages(full_text=True)
	http = urllib3.PoolManager()

	for m in dms:
		if len(m.text) > 140:
			mres = api.send_direct_message(m.sender.screen_name, text="Oops. Your grievance is longer than 140 characters, please try again.")
			print("LONG "+m.text)
			r = http.request('GET',GFORM_URL+quote("LONG "+m.text))
		else:
			mres = api.send_direct_message(m.sender.screen_name, text="Thanks, your grievance has been queued for approval.")
			print(m.text)
			#Grievances are tabulated annoymously in a Google Form where they are eventually posted
			#This part of the process will be automated in future version
			r = http.request('GET',GFORM_URL+quote(m.text))

		#Destroy the message received and the response to it
		api.destroy_direct_message(m.id)
		api.destroy_direct_message(mres.id)
	print("Done")

except:
	print("Could not connect to Twitter")
