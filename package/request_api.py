#! /usr/bin/env python3.3

import urllib.request
from datetime import date
from bs4 import BeautifulSoup

class RequestParamBuilder:

    GAME_BADMINTON = '18'
    NOON = 12
    
    def __init__(self, request_parameters):
        self.game_date = request_parameters.game_date
        self.start_time = request_parameters.start_time
        self.end_time = request_parameters.end_time
        self.location_code = request_parameters.location_code
        self.view_state = request_parameters.view_state
        self.event_validation = request_parameters.event_validation
        
    def build_http_param(self):
        play_date = self.game_date.strftime('%d/%m/%Y')
        validate_hidden_date = self.game_date.strftime('%m/%d/%Y')
       
        start_time_meridian = 'AM'
        end_time_meridian = 'AM'

        if self.start_time >= self.NOON:
            start_time_meridian = 'PM'
            if self.start_time > self.NOON: self.start_time = self.start_time - self.NOON  # Normalize

        if self.end_time >= self.NOON:
            end_time_meridian = 'PM'
            if self.end_time > self.NOON: self.end_time = self.end_time - self.NOON 

        if self.start_time < 10: self.start_time = '0' + str(self.start_time)

        if self.end_time < 10: self.end_time = '0' + str(self.end_time)
           
        req_params = urllib.parse.urlencode({'ctl00$ScriptManager1':'ctl00$ContentPlaceHolder1$updPnlAvailabilityCheck|ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$btnSearch', \
            'ctl00$wctrlLogin$Login1$UserName':'', \
            'ctl00$wctrlLogin$Login1$Password':'', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$ddlActivity': self.GAME_BADMINTON, \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$ddlVenue': self.location_code, \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$textBox':play_date, \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$hidden':play_date, \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$validateHidden':validate_hidden_date, \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$enableHidden':'true', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlStart$ddlHour': self.start_time, \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlStart$ddlMin': '00', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlStart$ddlMeridian': start_time_meridian, \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlEnd$ddlHour': self.end_time, \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlEnd$ddlMin': '00', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlEnd$ddlMeridian':end_time_meridian, \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfListSearchType':'ORD', \
            'ctl00$RESET_SESSION':'NIL', \
            'ctl00$AccNm':'', \
            'ctl00$hdfErrMsgAJAX':'', \
            '__REFRESH_FIELD':'439da2a090068a55acc3954d1d300266', \
            '__EVENTTARGET':'', \
            '__EVENTARGUMENT':'', \
            '__LASTFOCUS':'', \
            '__VIEWSTATE': self.view_state, \
            '__PREVIOUSPAGE':'dT7sUn7RZVoZ41GfdHOkMywZstCj-Ew5TKVOHQWYKDKw9tNTKN_JsTvJcvfohl8zkLUMHEQfAKHBuyJ_XoXLaB4v3fEZOIVcqgKnrkWn1RXqxduBcnyTwzOexdRD42xx9lQqJw2', \
            '__EVENTVALIDATION':self.event_validation, \
            '__ASYNCPOST':'true', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$btnSearch':'Search'})

        # build the http request
        req_params = req_params.encode('utf-8')

        return req_params

'''
A container for the http request parameters
'''
class RequestParameters:
    
    def __init__(self):
        self.game_date = ''
        self.start_time = ''
        self.end_time = ''
        self.location_code = ''
        self.view_state = ''
        self.event_validation = ''
        

'''
This class retrieves the __EVENTVALIDATION and __VIEWSTATE token from the initial page to be used in the subsequent
request for get available slots.
'''
class RequestTokenExtractor:
    
    def __init__(self):
        self.event_validation = ''
        self.view_state = ''

    def get_request_tokens(self):
        #The first request
        request = urllib.request.Request("http://www.icanbook.com.sg/icbnew/Facility/Public/UI/AvailabilityCheck.aspx")
        request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
        request.add_header("Referer", "http://www.icanbook.com.sg/icbnew/Facility/Public/UI/AvailabilityCheck.aspx")
        request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36")
        request.add_header("X-MicrosoftAjax", "Delta=true")

        f = urllib.request.urlopen(request)
        response = f.read().decode('utf-8')
        soup = BeautifulSoup(response.encode('utf-8'))
        
        view_state = soup.select('#__VIEWSTATE')[0]['value']
        event_validation = soup.select('#__EVENTVALIDATION')[0]['value']
                
        current_date = date.today().strftime('%d/%m/%Y')
        validate_current_date = date.today().strftime('%m/%d/%Y')
        
        #Simulate event selection
        req_params = urllib.parse.urlencode({'ctl00$ScriptManager1':'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$updPnlAvailabilityCheckCtl|ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$ddlActivity', \
            '__EVENTTARGET':'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$ddlActivity', \
            '__EVENTARGUMENT':'', \
            '__LASTFOCUS':'', \
            '__VIEWSTATE': view_state, \
            '__PREVIOUSPAGE':'dT7sUn7RZVoZ41GfdHOkMywZstCj-Ew5TKVOHQWYKDKw9tNTKN_JsTvJcvfohl8zkLUMHEQfAKHBuyJ_XoXLaB4v3fEZOIVcqgKnrkWn1RXqxduBcnyTwzOexdRD42xx9lQqJw2', \
            '__EVENTVALIDATION':event_validation, \
            'ctl00$wctrlLogin$Login1$UserName':'', \
            'ctl00$wctrlLogin$Login1$Password':'', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$ddlActivity':'18', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$ddlVenue':'0', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$textBox':current_date, \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$hidden':current_date, \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$validateHidden':validate_current_date, \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$dateCtl$CalendarPopup1$enableHidden':'true', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlStart$ddlHour':'06', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlStart$ddlMin':'00', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlStart$ddlMeridian':'PM', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlEnd$ddlHour':'10', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlEnd$ddlMin':'00', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$timeCtlEnd$ddlMeridian':'PM', \
            'ctl00$ContentPlaceHolder1$AvailabilityCheckCtl$hdfListSearchType':'ORD', \
            'ctl00$RESET_SESSION':'NIL', \
            'ctl00$AccNm':'', \
            'ctl00$hdfErrMsgAJAX':'', \
            '__REFRESH_FIELD':'1a66b8eba054759d798843c095737b5a', \
            '__ASYNCPOST':'true'});
            
        #Build the http req 
        request = urllib.request.Request("http://www.icanbook.com.sg/icbnew/Facility/Public/UI/AvailabilityCheck.aspx", data=req_params.encode('utf-8'), method='POST')
        request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
        request.add_header("Origin","http://www.icanbook.com.sg")
        request.add_header("Cookie","BIGipServerweb_pool_http=JiiuKjZyI/MyXXUtsjus9dXCDEp3VECVjVNDuJP+RVWxYegxCVsdA92TaFnqkBHA6LIK/++0W6ioW04=; ASP.NET_SessionId=3x24ih45ozjftxeg5py0mb45; __utma=24707618.545845258.1373292469.1373292469.1373292469.1; __utmc=24707618; __utmz=24707618.1373292469.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)")
        request.add_header("Referer","http://www.icanbook.com.sg/icbnew/Facility/Public/UI/AvailabilityCheck.aspx")
        request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36")
        request.add_header("X-MicrosoftAjax","Delta=true")

        f = urllib.request.urlopen(request)
        event_selection_response = f.read().decode('utf-8')
        
        self.view_state = self.__get_token_from_pdr('__VIEWSTATE', event_selection_response)
        self.event_validation = self.__get_token_from_pdr('__EVENTVALIDATION', event_selection_response);
        
        
    '''
    Internal method. Do not use.
    
    Retrieve the value of the specified token from a pipe delimited response
    '''
    def __get_token_from_pdr(self, token_name, partial_html_response):
        soup_parser = BeautifulSoup(partial_html_response.encode('utf-8'))
        partial_html = soup_parser.prettify()
        start_index = partial_html.find(token_name);
        sub_str = partial_html[start_index + (len(token_name) + 1) : len(partial_html)]
        
        end_index = 0
        for i, val in enumerate(sub_str):
            if val == '|':
                end_index = i
                break
            
        sub_str = sub_str[0 : end_index]
        
        return sub_str
        