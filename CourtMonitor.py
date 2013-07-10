#! /usr/bin/env python3.3

from twitter import *
from datetime import datetime

from package.venue_checker import VenueChecker

#Setup the request parameters

OAUTH_TOKEN = '1558071919-2XMmBP4GSphhiaz2uOZpBZmMdFIj76qlQYB6Xry'
OAUTH_SECRET = 'Ogs3MEmUF10wXcEG9mpMp9TpIlBXytVcyYEU2IqTtY'
CONSUMER_KEY = 'uNN3wAoVE0CVKMQss1w'
CONSUMER_SECRET = '6Ta6vHITkwbujGLVnIzb1XMjXqUXVhvKTz7VZ3s4sE'
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

#t.direct_messages.new(user='twitting4fun',text='first tweet from pi')

today = datetime.today()

#t.statuses.update(status="Checking for available court commencing at " + today.strftime("%d/%m/%Y %H:%M:%S"))
print("Checking for available court commencing at " + today.strftime("%d/%m/%Y %H:%M:%S"))
venue_checker = VenueChecker('542')
venue_checker.find_available_time()

