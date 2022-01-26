from datetime import datetime

class Error_logger:
    #class which oversees writing error information to error_log.txt

    def __init__(self):
        #creates an instance of error_logger, sets default values
        self.ident = 'NONE'
        self.timecon = 'NONE'
        

    def time_set(self):
        #retrieves current date and time, formats for use in scribe()
        time = datetime.now()
        yr = time.year
        yr = str(yr)
        mon = time.month
        mon = str(mon)
        dy = time.day
        dy = str(dy)
        hr = time.hour
        hr = str(hr)
        mn = time.minute
        mn = str(mn)
        self.timecon = '[' + mon + '/' + dy + '/' + yr + ' ' + hr + ':' + mn + ']'

    def scribe(self,ident):
        #takes ident from the calling file and writes information to a txt file
        self.time_set()
        with open('error_log.txt', 'at') as error_data:
            print(f'{self.timecon} {ident}', file=error_data)
