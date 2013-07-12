#! /usr/bin/env python3.3

from datetime import datetime

from package.venue_checker import VenueChecker
from package.location import LocationGenerator

#Setup the request parameters

'''
OAUTH_TOKEN = ''
OAUTH_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
'''

#t.direct_messages.new(user='twitting4fun',text='first tweet from pi')

today = datetime.today()

#t.statuses.update(status="Checking for available court commencing at " + today.strftime("%d/%m/%Y %H:%M:%S"))
print("Checking for available court commencing at " + today.strftime("%d/%m/%Y %H:%M:%S"))

loc_generator = LocationGenerator()

for location in loc_generator.get_locations():
    venue_checker = VenueChecker(location)
    query_result = venue_checker.find_available_time()
    
for result in query_result:
    for available_court in result:
        print(available_court.court_num, ' - ', available_court.time_slot, ' - ', available_court.status)


