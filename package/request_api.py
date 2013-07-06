#! /usr/bin/env python3.3

import urllib.request
import time
from datetime import date

class HttpRequestBuilder:

    GAME_BADMINTON = '18'
    NOON = 12
    
    def __init__(self, game_date, start_time, end_time, location_code):
        self.game_date = game_date
        self.start_time = start_time
        self.end_time = end_time
        self.location_code = location_code
        
    def build_http_request(self):
        play_date = self.game_date.strftime('%d/%m/%Y');
        validate_hidden_date = self.game_date.strftime('%m/%d/%Y');
        start_time_mm = '00';
        end_time_mm = '00';

        start_time_meridian = 'AM'
        end_time_meridian = 'AM'

        if self.start_time > self.NOON:
            start_time_meridian = 'PM'
            self.start_time = self.start_time - self.NOON #Normalize

        if self.end_time > self.NOON:
            end_time_meridian = 'PM'
            self.end_time = self.end_time - self.NOON 
        
        req_params = urllib.parse.urlencode({'ctl00$ScriptManager1':'ctl00$ContentPlaceHolder1$updPnlAvailabilityCheck|ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$btnSearch',\
            'ctl00$wctrlLogin$Login1$UserName':'',\
            'ctl00$wctrlLogin$Login1$Password':'',\
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$ddlActivity': self.GAME_BADMINTON,\
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$ddlVenue': self.location_code,\
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$textBox':play_date,\
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$hidden':play_date,\
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$validateHidden':validate_hidden_date,\
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$enableHidden':'true',\
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlStart$ddlHour': self.start_time,\
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlStart$ddlMin': start_time_mm,\
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlStart$ddlMeridian': start_time_meridian,\
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlEnd$ddlHour': self.end_time,\
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
            '__REFRESH_FIELD':'e80529539e5e910d9092c020a40e16b0',\
            '__EVENTTARGET':'',\
            '__EVENTARGUMENT':'',\
            '__LASTFOCUS':'',\
            '__VIEWSTATE':'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',\
            '__PREVIOUSPAGE':'dT7sUn7RZVoZ41GfdHOkMywZstCj-Ew5TKVOHQWYKDKw9tNTKN_JsTvJcvfohl8zkLUMHEQfAKHBuyJ_XoXLaB4v3fEZOIVcqgKnrkWn1RXqxduBcnyTwzOexdRD42xx9lQqJw2',\
            '__EVENTVALIDATION':'IHc65VENpg9phGUNEr2eX9ZQGgFIy5BUYY+c87Rj2PB6oeG1kK2MPJvvX4FGTpSOiTbsz8XkQfs5HvfG6CUbJ6/2TCD+ssfnNSOMqP4wW8AbKwLuz2YOepIht4/RG61x9SRvzGkXfOZ6hk8+6ezWKb00pfis228DiqEy3bsYu7ZgBZai9Mliyka2PBvAXMfOiUTfjMSvqVUXtu9PACi+coa/ncCNkDlsPj+xLC5C9u+HDLv+hIfAQZGcBTmVR2N4GZE7jO+7vIR2J7tZJGcyviyye9ckEpGINpxu0hhJ/bavkwijV0DinoQ8ZQJzHbVJ4olcxwLzw1cWm/abYuRQ1Idx3gH2WjS4ju6ZC2MJUQgxETCuhXr0YIXYeRqNUx7VbITZmTwvXdw5oWfdEiClYEKjROLF+NVOFcmm1dnVsUwUFbwMZ4kVPhVx/dPuTkmGxLfsEdl0kMJ6T9sgq5AmE4jxPxFErPdClXRExqfnsBegh4ObkYv4C1AivDdtopnB/Xhz+GVHycHPosmbZN4OgFZpBXwxg1BszdftvzO+ErE3byGOWzpNERrg/bnqt9qvxN50HAFL5mj1ElvPl0OdVWeGwR8Clizxy6mgJPTPpKzWlzO4PVzQ5JHNcZ5rSh3Q0P88xNIv/WkCF8MvCOTzkZVEtvmJ2JKNaJUewdgH+x1fngwlbo5cR1Z0XLjzNSAV5X02hzt923HMxV2pFU1uq8k/WcY9gyRpF4C9vB/GwvCKVsI2TEQxxVfyU3XQVzfRqHrV5HUBqzMxPjTwP9wo7vTS+/KN9Z6D9d2T2jp5zMDJHwo4/n+98OH9TPY39P2YfYgxc5FrEwlruUTD715G9l0Jr9cJhZhrvTYqFg4vNmRg3H2A9Ze5ecaqBatm7WpjyvM0/I+g5iLT9KE9r+upguWMsx6VbtjhP5gqbQ4EAknNcAdcUPn+Pxol04I9YG3Uq+PdQDHK7qcsXgRcSXswkFaqvqlLQcEcHBvHBfOJPg6QpN3L2Aa2lffRsYVCqhNa4l4sezB0JKAuIlkrL0fixsN9hKlmnLU37ppBRgQIlvr+qmlKdLQID2B5fBLnluG8JwqlA1v/z/FWrG/oYmfgINmwNMiozNuk0eXvIHEoFnUHPE0u5ekme8MEN5J1xKgKP9thpcn9A/nm8FiTyHRqHju1drCyYFg4YCQys8dBZ/2ley3iXWmkdoSB2AX8cQZOe34sBNA0PRJ74KGPfbl4j1bylKxit5+zO8I60+j2veQ1ksIDpCF1v8rsUu9TeSyQMHFUvS7iRo3aRTDJJup7+AoLgORnkvFf5dNdHiOhXx9QBHkFiSEbmkKonsRCIYHILg+yTekofa82SkBT8F1MwqMtNG2tRMzurPexXwQdr3KCIfuNDu47mSGm4h6zeC5RStYsexrjr6vs5MhzkrEO1ADGOwKQQTulkG2lJdSc7RCnCS1pYJq8xDP0FVXEQ0Gp35ONRhKrw5DYp45/6JQN2DlgQL63mYSTQFt+dYeo4QIRWYGAPw3TYeOfQm2NBeR0kXz7dfXxQnYWM/sPysh+65o+yfinX4hr2JxdnN1UqxGH+lbhDFV0ol7W8h8KaRqLEFxF2913nkNP5xfTpC/4cmFCC6mfs0LJG5SXtD1wp7jLYSUF2f5pAPzqKAyl//VRWORfHPjdBs+Rc0N4fUcZkzHLTq+IEKXa0cFQEfdWl2CxKgE2xpxkEKwH3k7K/i1GXHEhtm8e9YIMsqWUHofYl9ZLlseu42vpuxBLonq0YCwBTaf5werpe+hSI7d95teLieGzrYAfTUVq9teGd/4p2DMYX0fN11JpRCnw/+ltSVGWBS3aRCQ5nszRl0YyH51VNYN7EAEzc5yQSlVF1vpiGArnFp8EG2bKNqAlY4v0hSe+sVTl6oyHhD242j0T57LFrLS76CcKSlLEB8fa0Qj2M3SV0FN89g/hSDurqHWr4tLw3QA9',\
            '__ASYNCPOST':'true',\
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$btnSearch':'Search'})

        #build the http request
        req_params = req_params.encode('utf-8');

        return req_params
