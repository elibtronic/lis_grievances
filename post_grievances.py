#!/usr/bin/env python3

import tweepy
from settings import *

#This file will look into the text file and post one tweet per go


# Try to connect to Twitter first

try:
	grieve_file = open(GTPATH,"r+")
	g = grieve_file.readline()
	if g != "":
		print(g)
		rest_g = grieve_file.read()
	
		grieve_file.seek(0)
		grieve_file.truncate()
		grieve_file.write(rest_g)
		grieve_file.close()
	
		#Only connect if there is something to post
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		api = tweepy.API(auth)
		api.update_status(g)

		print("Done")
	else:
		print("Grievance did not post")

except:
	print("No Grievances to Air")
	pass

