#! /usr/bin/env python3.3

from datetime import date,timedelta

class TimeGenerator:
    '''
    Valid game time constants. We can only play from 9am - 7pm
    '''
    valid_time_values = [8,9,10,11,12,13,14,15,16,17,18,19,18,19,20]
    
    START_TIME = 9
    END_TIME = 20
    
    def __init__(self):
        self.start_time_index = 0

    '''
    Retrieves a two-hour time frame
    '''
    def get_game_time_frame(self):
        time_range_list = list();
        for time in range(self.START_TIME, self.END_TIME, 2):
            time_range_list.append(TimeRange(time, time + 2))

        return time_range_list


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
        
        for x in range(15):
            today = today + timedelta(days=1)
            if today.weekday() == self.SATURDAY or today.weekday() == self.SUNDAY:
                date_list.append(today);

        return date_list
    
