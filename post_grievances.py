#!/usr/bin/env python3

import tweepy, re, urllib.request,os
from settings import *

#This file will look into the text file and post one tweet per go


# Try to connect to Twitter first

try:
	grieve_file = open(GTPATH,"rb+")
	g = grieve_file.readline()

	if len(g) != 0:
		rest_g = grieve_file.read()
		grieve_file.seek(0)
		grieve_file.truncate()
		grieve_file.write(rest_g)
		grieve_file.close()
	
		#Only connect if there is something to post
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		api = tweepy.API(auth)

		
		#If we have a URL with a JPG or GIF ending we want to post it		
		try:
			g_string = str(g.decode("unicode_escape"))
			m_url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',g_string)[0]
			m_fn = IMG_CACHE+m_url.rsplit('/')[-1]
			m_ext = m_fn[-4:]
		except:
			m_ext = ""
			m_fn = ""
		


		#Check/download media then post
		if (m_ext == ".gif" or m_ext == ".jpg" or m_ext == ".png"):

			g_text = b' '.join(g.split(b' ')[1:])
			resp = urllib.request.urlretrieve(m_url,m_fn)			
			print("Media tweeting: "+str(g_text))
			api.update_with_media(m_fn,g_text)
			os.remove(m_fn)
		else:
			print("Tweeting: "+str(g))
			api.update_status(g)

		print("Done")
	else:
		print("No Grievance to post")
		exit()

except Exception as e:
	print("Did not post, caught exception ",e)
	pass


# Delete any lingering DMs by borking them
#try:
#        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#        api = tweepy.API(auth)
#        dms = api.direct_messages()
        # The nuclear option, will delete all DM's to the bot.
#        for m in dms:
#                print("Passing on bork")
#                api.destroy_direct_message(m.id)
#        print("Done Borking")
#except:
#        print("Could not connect to twitter to bork")

