
# LIS Grievances #

![george](./html/george.jpg)

*Because we all need to air our grievances some time*

## Setup ##

### OPTIONAL: Web files ###

- Install apache/nginx etc to display the web component
- Modify the html files to point to your account and avatar
- run `sudo ./deploy_html` to copy those files to the usual **/var/www/html**


### Next ###

- create your *_grievances* account on twitter
- be sure to add a [Mobile](https://twitter.com/settings/add_phone) number as well or you won't get an API key
- run `install_pre` as  **sudo** to install necessary parts
- generate [Twitter API](https://apps.twitter.com/) key
- be sure to allow access to DM in APP settings (see fig 1)
- Create a Google Form with one text box and get a pre-filled URL to serve as protoype, check settings for details
- add relevate info to **settings.py**
- add `check_grievances.py` to crontab to fire at a resonable time frame (once an hour)

![figure_1](./new_app.png)





An art project by [@elibtronic](https://twitter.com/elibtronic)

[elibtronic.ca](https://elibtronic.ca)
