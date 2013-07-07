#! /usr/bin/env python3.3

from datetime import date,timedelta

class TimeGenerator:
    '''
    Valid game time constants. We can only play from 9am - 5pm
    '''
    valid_time_values = [8,9,10,11,12,13,14,15,16,17,18,19]
    
    def __init__(self):
        self.start_time_index = 0

    '''
    Retrieves a two-hour time frame
    '''
    def get_game_time_frame(self):
        
        # Check if the index pointer is at the 2nd to the last position
        if self.start_time_index == len(self.valid_time_values) - 2:
           self.start_time_index = 0 
        
        #Create new TimeRange object
        time_range = TimeRange(self.valid_time_values[self.start_time_index], \
                               self.valid_time_values[self.start_time_index + 2])
        
        #Move the index pointer 1 position forward
        self.start_time_index += 1

        return time_range


'''
The TimeRange class. Defines a range of time in 24 hour format.

Examples:
1. time_range = TimeRange(9,11); #Creates a TimeRange object from 9am - 11am
1. time_range = TimeRange(11,13); #Creates a TimeRange object from 11am - 1pm
1. time_range = TimeRange(17,19); #Creates a TimeRange object from 5pm - 7pm
'''
class TimeRange:
    
    def __init__(self, start_time, end_time):
        self.start_time = start_time;
        self.end_time= end_time


'''
Identifies the dates of the first and second saturdays and sundays from the
current date
'''
class GameDateGenerator:

    SATURDAY = 5;
    SUNDAY = 6;
   

    '''
    Returns a list containing the first and second saturdays and sundays from the current date.
    Example:
    if date.today() supposedly returns 04-07-2013 which is a thursday. This method will return
    a list containing the following values in order:

    06-07-2013
    07-07-2013
    13-07-2013
    14-07-2013
    
    '''
    def get_game_date(self):
        date_list = list();
        today = date.today()
        
        while len(date_list) < 4:
            today = today + timedelta(days=1)
            if today.weekday() == self.SATURDAY or today.weekday() == self.SUNDAY:
                print(today.strftime('%d/%m/%Y'));
                date_list.append(today);

        return date_list
    