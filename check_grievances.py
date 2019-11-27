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

	#Posts come in as unicode characters, prints ascii safe version to the screen

	for m in dms:
		#for screen debugging
		m_clear = m.text.encode("utf-8")

		if len(m.text) > 280:
			mres = api.send_direct_message(m.sender.screen_name, text="Oops. Your grievance is longer than 280 characters, please try again.")
			print("LONG "+m_clear)
			r = http.request('GET',GFORM_URL+quote("LONG "+m.text))
		else:
			mres = api.send_direct_message(m.sender.screen_name, text="Thanks, your grievance has been queued for approval.\n\n More details here: http://lisgrievances.com/about.html")
			print(m_clear)
			#Grievances are tabulated annoymously in a Google Form where they are eventually posted
			#This part of the process will be automated in future version
			r = http.request('GET',GFORM_URL+quote(m.text))

		#Destroy the message received and the response to it
		api.destroy_direct_message(m.id)
		api.destroy_direct_message(mres.id)
	print("Done Checking")

except Exception as e:
	print("Exception: ",e)
	print("Could not connect to Twitter to check")
	exit()


# Delete any lingering DMs by borking them
#try:
#	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#	api = tweepy.API(auth)
#	dms = api.direct_messages()
	# The nuclear option, will delete all DM's to the bot.
#	for m in dms:
#		print("pass")
#		api.destroy_direct_message(m.id)
#	print("Done Borking")
#except:
#	print("Could not connect to twitter to bork")
