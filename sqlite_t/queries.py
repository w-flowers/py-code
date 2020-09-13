import sqlite3

import time



def create_default_date():
    
    newtime = time.localtime()
    
    year = newtime.tm_year
    
    month = newtime.tm_mon
    
    day = newtime.tm_mday
    
    hour = newtime.tm_hour
    
    minute = newtime.tm_min
    
    second = newtime.tm_sec
    
    result = str(year)+"-"+str()

class Record:
    
    def __init__(self, email, name, org = "NULL", sign_up_date = create_default_date(), groups = []):
        
        self.email = email
        self.name = name
        self.org = org
        self.sign_up_date = sign_up_date
        self.groups = groups
    
    #Creates the necessary SQL command to enter the record into the database
    def prepare_entry_query(self, table_name):
        
        instruction = "INSERT INTO "
        
        instruction.append(table_name + " VALUES ")
        
        instruction.append("("+ self.email + ", " self.name + ", ")
        
        instruction.append( + self.org + ", " + ", " + self.date + ")")
        
        
        
        return instruction
        
        
        