#! /usr/bin/env python3.3

from bs4 import BeautifulSoup
'''
Parser for the Http Response
'''
class ResponseParser:

    '''
    Parses the Http Response and returns a list of CourtStatus if
    it finds a court status not equal to 'Not Available Slot'
    '''
    def parse_response(self, date, resp, description):
        response = resp.read().decode('utf-8');
        soup = BeautifulSoup(response.encode('utf-8'))
        result_table = soup.select('#ctl00_ContentPlaceHolder1_gvAvailabilityCheckResult tr')

        #print(soup.prettify())

        available_court = list();
        for child in result_table :
            img_list = child.select('td img')
           
            if(len(img_list) > 0 ) :
                court_num = child.select('td span')[0]
                time_slot = child.select('td span')[1]
                status = img_list[0]['title']
                #print(court_num.text, ' ', time_slot.text, ' ', status)
                if status != 'Not Available Slot':
                    print('Probable location found on ', date.strftime('%d/%m/%y'), time_slot.text, ' at ', description, ' ', court_num.text, ' status ', status)
                    available_court.append(CourtStatus(date, description, court_num.text, time_slot.text, status))
                
        return available_court


class CourtStatus:

    def __init__(self, date, location, court_num, time_slot, status):
        self.date = date
        self.location = location
        self.court_num = court_num
        self.time_slot = time_slot
        self.status = status
