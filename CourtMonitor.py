#! /usr/bin/env python3.3

import urllib.request,urllib.parse
from bs4 import BeautifulSoup
from twitter import *
from package import *
from datetime import datetime

#Setup the request parameters

play_date = '21/7/2013'
validate_hidden_date = '7/21/2013'
start_time_hh = '04'
start_time_mm = '00'
start_time_meridian = 'PM'
end_time_hh = '06'
end_time_mm = '00'
end_time_meridian = 'PM'

#Activity 18 - Badminton,Venue 542 - Pasir Ris 
req_params = urllib.parse.urlencode({'ctl00$ScriptManager1':'ctl00$ContentPlaceHolder1$updPnlAvailabilityCheck|ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$btnSearch',\
'ctl00$wctrlLogin$Login1$UserName':'',\
'ctl00$wctrlLogin$Login1$Password':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$ddlActivity':'18',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$ddlVenue':'542',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$textBox':play_date,\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$hidden':play_date,\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$validateHidden':validate_hidden_date,\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$enableHidden':'true',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlStart$ddlHour': start_time_hh,\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlStart$ddlMin': start_time_mm,\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlStart$ddlMeridian': start_time_meridian,\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlEnd$ddlHour': end_time_hh,\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlEnd$ddlMin': end_time_mm,\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlEnd$ddlMeridian':end_time_meridian,\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfBookAdv':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfIsSuperiorSubscriber':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfVenueSubscriberType':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfListSearchType':'ORD',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdRepSubscriberId':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdRepActivityId':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdRepSubscriberName':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdRepActivityName':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdIsReplacement':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdIsReplacementReload':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdRepBkgCancelledId':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfCriteriaNotMatch':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfIsBlacklistedHirerBook':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfEffDateFrom':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfEffDateTo':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfIsAdvHrBookingAllowed':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfLeadTimeAccess':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfSubscriberId':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfHirerAge':'',\
'hidPrinterStatus':'',\
'hidPrinterVerification':'',\
'hidNetsStatus':'',\
'hidNetsVerfication':'',\
'hidEzlinkStatus':'',\
'hidEzlinkVerification':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfHiredId':'',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfHirerType':'',\
'ctl00$ContentPlaceHolder1$hdRblSelectedValue':'',\
'ctl00$ContentPlaceHolder1$hidAvailTerminals':'',\
'hidAvailTerminalsId':'ctl00_ContentPlaceHolder1_hidAvailTerminals',\
'ctl00$RESET_SESSION':'NIL',\
'ctl00$AccNm':'',\
'ctl00$hdfErrMsgAJAX':'',\
'__REFRESH_FIELD':'2781e6abbd661d845107066b1c6b00a3',\
'__EVENTTARGET':'',\
'__EVENTARGUMENT':'',\
'__LASTFOCUS':'',\
'__VIEWSTATE':'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',\
'__PREVIOUSPAGE':'dT7sUn7RZVoZ41GfdHOkMywZstCj-Ew5TKVOHQWYKDKw9tNTKN_JsTvJcvfohl8zkLUMHEQfAKHBuyJ_XoXLaB4v3fEZOIVcqgKnrkWn1RXqxduBcnyTwzOexdRD42xx9lQqJw2',\
'__EVENTVALIDATION':'hSuEHUING0T+FLAMiTllEUaAr3/YUp4c03Ec33zKGcne/gJ+uqmFhJ8QBqyH4G42hnl4EclMcWB1FE5rTqGloNdb/mk7qCUNHe/xeJl7BrknlpLTcD5y2e/2o58jwx8tUROQ+mVq8NGiJn6GOFIc5yO7egKiAR4D4qkkMd2iHTgfOKOpWWIW2L1yoUPaqCERvDQTuDyPjhCRI9Q/AHw7SWV139XrLxcpVpcKSMHNsDoCNe1jl/yAxCfeGWlNz6xuNVO8URN2TnbDoWe4ehWrn9uk0PUhlnA7Gxzdpf69fawea4H0tSc2BsyeH9mzwlXiLHggCUWUA6tcCr6WzTescJwAL43FPDtO7Ary0ctsoi7DkGHypDqftt+td0PL0fMpzIX4jy2YxEDN8i6CqmLAXHtygygy0Dgc2aIqE1f7zRZlb6I+M9v/uDdz3Y58mzRQ2wlmwjnoOlhDeKLtxaYkgrSNlL9W9YKnlEKw6XF7g03tO9c9HFM+Qz3wxMxKqNjMA5lEUjOAevqsybLFdaSNCYWnjt9e9O0g8hHyGDnYx2FgY9t4+WJ97vQN3Y5lQ9yR/EIzq1fCSPsPiaurToyiJhJBIrSlufm451tJX0LJdbZ1Wcz70S8oK/yajBx7wRl9lOCSe/4zLk4lKnapgrufQFyu+bS0Y0i12tXP1xdtSpSQdXH0Nn2IPtCS0AHxqMEt5dd6H+1YepI4i5R/mgRsSTrfvPwv3f9DPG34GYBp2j7wKni+EzfOdTI8bd/NmK0UR2K2Hz1Um/RtRqi4lBkyZ3DZd7NWfJvVYSAL+m2CA/yPor57QP8K3t8yZvCNiyS3SXXuwK/hF9/nVyuLrpRt/olPCkMfz8ZFDZud6QpFY/cDo8PY4/DF1NAQL02YrWsIaLyJg+NsjQbr/PMwy3mvTWhpAZ0DYzAwmb3GILCBrUg+dzRrLlF7Q2Yo6Q0h3Fx6xGOLWgefMNN8GkUbBz6xKpc727fJyM1fgd+PdAY0lHncKSXaw4++dLv6Jiw2P93yOd8nIbk6mCpYDnzS0M382dEZY/7aDd/2J2sePsawLbd21srRJc9Aec6ODY9IsLASgJNiyNveLsa+YxmPc97OyLAWDoOxODV5JRAc/oJvwsrqxKY3UO2qQ1pgMy+MoQoeOakf9+7CgGukCOc9/uK9LqCXHTXEnGnpTTdf/3d1oO7MkEQmM+kt8Ej6+25IgGabXXcuvnKDyMiwz1KLRV+n+Kmmh4NF437NYqJ+TWTwAajXIfbfP+tLyH3TD/MIs8IXO4OmxqUffiFjN6xfZ3jNmj3oBxsrf3FeVKwClFSLvMflzKPjTHE+Qy1jiFuH/Q7mVLCRGQ5/BagK3Tt4zbxlzna57kh530LioW9wD8e8bExGILPIaO+Cd1sQ4ZCG4dEQZeiwz1CJuGLvNNmn9inbQYkPqLUsiAZtpdaZICIpguXAv9y6SjjEy6fInPOploe7cZ5rMXh6hb7+NIhKYn7E3sLuwMw70TUTaRxiacRoGJEHFhbI7eexjdNFvqeNOhn1EEAYKkc8HwwFFJTPhk1MDBdz6HZYmg3wgb1giHMTaNQTqGNFDAsyiqSo4SPCt49Dx/otH1fMuMCml6KsIoi8KrAFT+HnpS0/BttnRgXEkJsBeB3HhxFHL9w67sREY+oWUCIPv7GaXDrHGHd2O4bCFrP+6siM3NJbOvF20xxYMVpTMnGoVNjs2b/tprQxhGXkV40bfb/qwLjzqPTDWrrt4yESIL8F/t5LRK4MjUFEuPkvKfndIHNK2JOn3J7FCMVPijB8KNnXWF5hj5sDX9G4I5GAPyrWOyWmZgkpOlNoMN2LyAGoOPBSHgMC1RZiy3kdMM9ROuicILdsdYI8JHylxYm5WJg+UcbTfP3/MLuFQY5jLfZeu1h04xlMAvHenrP42vcH25T65fxDqhgpE19tIGiCEXO6M44Hrd1gipxILgXc7YsQNfyWBxlHOy6Hz+Cs1KWNyw==',\
'__ASYNCPOST':'true',\
'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$btnSearch':'Search'})

#build the http request
req_params = req_params.encode('utf-8')
request = urllib.request.Request("http://www.icanbook.com.sg/icbnew/Facility/Public/UI/AvailabilityCheck.aspx")
request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
request.add_header("Referer","http://www.icanbook.com.sg/icbnew/Facility/Public/UI/AvailabilityCheck.aspx")
request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36")
request.add_header("X-MicrosoftAjax","Delta=true")

#open the connection
f = urllib.request.urlopen(request, req_params)

#Parse the response
response = f.read().decode('utf-8')
soup = BeautifulSoup(response.encode('utf-8'))
#print(soup.prettify())
result_table = soup.select('#ctl00_ContentPlaceHolder1_gvAvailabilityCheckResult tr')

OAUTH_TOKEN = '1558071919-2XMmBP4GSphhiaz2uOZpBZmMdFIj76qlQYB6Xry'
OAUTH_SECRET = 'Ogs3MEmUF10wXcEG9mpMp9TpIlBXytVcyYEU2IqTtY'
CONSUMER_KEY = 'uNN3wAoVE0CVKMQss1w'
CONSUMER_SECRET = '6Ta6vHITkwbujGLVnIzb1XMjXqUXVhvKTz7VZ3s4sE'
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

for child in result_table :
    img_list = child.select('td img')
    if(len(img_list) > 0 ) :
        court_num = child.select('td span')[0]
        time_slot = child.select('td span')[1]
        print(court_num.text + ' '+ time_slot.text + ' '+ img_list[0]['title'])
        print('===============================')


#t.direct_messages.new(user='twitting4fun',text='first tweet from pi')

time_generator = TimeGenerator()
date_generator = GameDateGenerator()

print(time_generator.get_game_time_frame().start_time)
print(date_generator.get_game_date())

today = datetime.today()

#t.statuses.update(status="Checking for available court commencing at " + today.strftime("%d/%m/%Y %H:%M:%S"))
print("Checking for available court commencing at " + today.strftime("%d/%m/%Y %H:%M:%S"))
#venue_checker = VenueChecker('542')
#venue_checker.find_available_time()

