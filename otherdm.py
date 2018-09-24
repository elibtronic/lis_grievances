#!/usr/bin/python3

import json
import os
import urllib3
from urllib.parse import quote
from settings import *


#I'm using RUBY for the love of...

os.system("twurl -X GET /1.1/direct_messages/events/list.json > dms.json")
dj  = json.loads(open("dms.json").read())


if "errors" in dj:
	print("Hit an error " + json.dumps(dj))
	exit()

if dj["events"] == []:
	print("nothing sent")
	exit()


for e in dj["events"]:

	message_id = e["id"]
	message_text = e["message_create"]["message_data"]["text"]
	
	print(message_text.encode("utf-8"))

        # Post to GF
	http = urllib3.PoolManager()
	if len(message_text) > 280:
		r = http.request('GET',GFORM_URL+quote("LONG "+message_text))
	else:
		r = http.request('GET',GFORM_URL+quote(message_text))
        #Delete Original
	del_line = "twurl -X DELETE /1.1/direct_messages/events/destroy.json?id="+message_id
	os.system(del_line)

os.remove("dms.json")
