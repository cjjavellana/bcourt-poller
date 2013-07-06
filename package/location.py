#! /usr/bin/env python3.3

class LocationGenerator:
    '''
    Paris Ris = 542
    Bedok = 291
    Hougang = 301
    '''
    LOCATION = [542,291,301]
    
    def __init__(self):
        self.location_index = 0

    def get_locations(self):
        return LOCATION
        
        
