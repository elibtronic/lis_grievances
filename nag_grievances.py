#!/usr/bin/env python3

import tweepy
from settings import *
from random import randint

#This file will post a nag to troll for more grievances
#Reads the nags in NAGLIST and chooses one at random


# Try to connect to Twitter first
try:
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)
except:
	print("Error Connecting to Twitter")
	exit

try:
	print(NAGLIST)
	nag_file = open(NAGLIST,"r")
	nags = nag_file.readlines()
	n = randint(0,len(nags)-1)
	print(nags[n].strip())
	api.update_status(nags[n].strip())
	print("...Done")

except:
	print("Could not nag")
	pass

