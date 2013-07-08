#! /usr/bin/env python3.3

from package import GameDateGenerator
from package import TimeGenerator
from package import RequestParamBuilder
from package import ResponseParser

import urllib.request,urllib.parse

'''
The class VenueChecker checks for available game slots for the
next saturdays and sundays from 9am - 7pm for the given location
code
'''
class VenueChecker:
    
    def __init__(self, location_code):
        self.location_code = location_code
        self.avail_time = []
        
    def find_available_time(self):
        date_gen = GameDateGenerator();
        game_dates = date_gen.get_game_date();

        response_parser = ResponseParser()

        slots = list()
        
        time_gen = TimeGenerator();
        for game_date in game_dates:
            for x in range(9):
                time_range = time_gen.get_game_time_frame()

                print('Checking ', self.location_code, '; Start Time: ', \
                      str(time_range.start_time), '; End Time: ', str(time_range.end_time))
                
                request_builder = RequestParamBuilder(game_date,time_range.start_time,time_range.end_time,self.location_code)
                req_params = request_builder.build_http_param();

                #Build the http req 
                request = urllib.request.Request("http://www.icanbook.com.sg/icbnew/Facility/Public/UI/AvailabilityCheck.aspx", data=req_params, method='POST')
                request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
                request.add_header("Origin","http://www.icanbook.com.sg")
                request.add_header("Cookie","BIGipServerweb_pool_http=JiiuKjZyI/MyXXUtsjus9dXCDEp3VECVjVNDuJP+RVWxYegxCVsdA92TaFnqkBHA6LIK/++0W6ioW04=; ASP.NET_SessionId=3x24ih45ozjftxeg5py0mb45; __utma=24707618.545845258.1373292469.1373292469.1373292469.1; __utmc=24707618; __utmz=24707618.1373292469.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)")
                request.add_header("Referer","http://www.icanbook.com.sg/icbnew/Facility/Public/UI/AvailabilityCheck.aspx")
                request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36")
                request.add_header("X-MicrosoftAjax","Delta=true")

                f = urllib.request.urlopen(request)
                print('parsing response...', f.read().decode('utf-8'))
                avail_slots = response_parser.parse_response(f)
                slots.append(avail_slots)


        return slots

