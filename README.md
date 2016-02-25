
# LIS Grievances #

![george](./html/george.jpg)

*Because we all need to air our grievances some time*

## Setup ##

### OPTIONAL: Web files ###

- Install apache/nginx etc to display the web component
- Modify the html files to point to your account and avatar
- run `sudo ./deploy_html` to copy those files to the usual `/var/www/html`


### Next ###

- create your *_grievances* account on twitter
- be sure to add a [Mobile](https://twitter.com/settings/add_phone) number as well or you won't get an API key
- generate [Twitter API](https://apps.twitter.com/) key
- be sure to allow access to DM in APP settings (see fig 1)- run `sudo ./install_pre` to install necessary parts (Currently just [tweepy](http://www.tweepy.org/)) and generate settings file
- Create a Google Form with one text box and get a pre-filled URL, check settings for details/example
- add relevate info about form and API account info to `settings.py`



### Checking Grievances ###

- add `check_grievances.py` to crontab to fire at a reasonable time frame (once an hour on the 30 minute mark)
- also `chmod +x` as well
- Grievances will be posted to your Google Spreadsheet

### Posting Grievances ###

- Your job is now to add the grievances from the spreadsheet to `hopper/grievances_to_air.txt`, ie. use some discretion
- add `post_grievances.py` to crontab to fire at a reasonable time frame (once an hour on the 00s)
- once again `chmod +x` might be necessary


![figure_1](./new_app.png)

**fig 1 **





An art project by [@elibtronic](https://twitter.com/elibtronic)

[elibtronic.ca](https://elibtronic.ca)
