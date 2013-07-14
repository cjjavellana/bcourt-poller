#! /usr/bin/env python3.3

from datetime import datetime

from package.venue_checker import VenueChecker
from package.location import LocationGenerator
from twitter.api import Twitter
from twitter.oauth import OAuth

#Setup the request parameters

key_file = open('encryption_key', mode='r')
for i,line in enumerate(key_file):
    if i == 0: OAUTH_TOKEN = line
    if i == 1: OAUTH_SECRET = line
    if i == 2: CONSUMER_KEY = line
    if i == 3: CONSUMER_SECRET = line
    
#t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
#t.direct_messages.new(user='twitting4fun',text='first tweet from pi')

today = datetime.today()

#t.statuses.update(status="Checking for available court commencing at " + today.strftime("%d/%m/%Y %H:%M:%S"))
print("Checking for available court commencing at " + today.strftime("%d/%m/%Y %H:%M:%S"))

loc_generator = LocationGenerator()

query_result = list()
for location,description in loc_generator.get_locations().items():
    print ('Checking location: ', description)
    venue_checker = VenueChecker(location,description)
    query_result.append(venue_checker.find_available_time())

# Display the mined data
for i in query_result:
    for j in i:
        for k in j:
            print(k.date.strftime('%d-%m-%y'), k.location,' ', k.court_num, ' - ', k.time_slot, ' - ', k.status)


