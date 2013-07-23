#! /usr/bin/env python3.3

from datetime import datetime

from package.venue_checker import VenueChecker
from package.location import LocationGenerator

def main():
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


#This is the standard boilerplate code that calls the main() function
if __name__ == '__main__':
    main()