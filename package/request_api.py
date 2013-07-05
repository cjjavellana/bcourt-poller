#! /usr/bin/env python3.3

import urllib.request
import time
from datetime import date

class HttpRequestBuilder:
    def __init__(self, game_date, start_time, end_time, start_time_meridian, end_time_meridian):
        self.game_date = game_date
        self.start_time = start_time
        self.end_time = end_time
        self.start_time_meridian = start_time_meridian
        self.end_time_meridian = end_time_meridian
        
        
    def build_http_request(self):
        req_params = urllib.parse.urlencode({})
    
