#!/usr/bin/env python

import tweepy
from settings import *

#This file will look into the text file and post one tweet per go


# Try to connect to Twitter first
try:
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
except:
	print "Error Connecting to Twitter"
	exit

try:
	grieve_file = open("hopper/grievances_to_air.txt","r+")
	g = grieve_file.readline()
	rest_g = grieve_file.read()
	
	grieve_file.seek(0)
	grieve_file.truncate()
	grieve_file.write(rest_g)
	grieve_file.close()
	
	if g != "":
		print g
		api.update_status(g)
		print "Done"
	print "Grievance did not post"

except:
	print "No Grievances to Air"
	pass

