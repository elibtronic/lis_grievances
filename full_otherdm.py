#!/usr/bin/env python3

import json
import os
import urllib3
from urllib.parse import quote
from settings import *

SPATH = "/home/grief/lis_grievances"

#I'm using RUBY for the love of...

os.system("twurl -X GET /1.1/direct_messages/events/list.json > /home/grief/lis_grievances/dms.json")
dj  = json.loads(open("/home/grief/lis_grievances/dms.json").read())



if "errors" in dj:
	print("Hit an error " + json.dumps(dj))
	exit()

if dj["events"] == []:
	print("nothing sent")
	exit()


for e in dj["events"]:

	message_id = e["id"]
	message_text = e["message_create"]["message_data"]["text"]
	sender_id = e["message_create"]["sender_id"]
	
	print(message_text.encode("utf-8"))

        # Post to GF
	http = urllib3.PoolManager()
	urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
	if len(message_text) > 280:
		r = http.request('GET',GFORM_URL+quote("LONG "+message_text))
	else:
		r = http.request('GET',GFORM_URL+quote(message_text))
        
	#Delete Original
	del_line = "twurl -X DELETE /1.1/direct_messages/events/destroy.json?id="+message_id
	os.system(del_line)

	#Send success message & delete it
	feedback_line = "twurl -A 'Content-type: application/json' -X POST /1.1/direct_messages/events/new.json -d '{\"event\": {\"type\": \"message_create\", \"message_create\":{\"target\": {\"recipient_id\": \""+sender_id+"\"}, \"message_data\": {\"text\": \"Thanks for submitting your grievance. It has been queued for approval.\"}}}}'"
	os.system(feedback_line+"> /home/grief/lis_grievances/to_del.json")
	del_mes = json.loads(open("/home/grief/lis_grievances/to_del.json").read())
	del_mes_id = del_mes["event"]["id"]
	del_res_line = "twurl -X DELETE /1.1/direct_messages/events/destroy.json?id="+del_mes_id
	os.system(del_res_line)
	os.remove("/home/grief/lis_grievances/to_del.json")


os.remove("/home/grief/lis_grievances/dms.json")
