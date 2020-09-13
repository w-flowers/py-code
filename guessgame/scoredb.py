# A simple database api for a game
# The game should pass in a username, a score and a time taken
# In addition to this info, the entry function will store the time the score is entered
# The return_stats and return_records functions will return a list of strings -  it is
# up to the calling function to use these.

import sqlite3
import time

def add_score_to_db(name, score, time_taken, db_path):
    conn = sqlite3.connect(db_path)
    
    curs = conn.cursor()
    
    entry_tup = (name, score, time_taken)
    
    curs.execute("""create table if not exists scores ('game_number' INTEGER PRIMARY KEY,
                   'username' TEXT, 'score' INTEGER, 'time_taken' REAL, 'date' TEXT)""")
    
    curs.execute("""insert into scores('username', 'score', 'time_taken', 'date') values (?, ?,
                    ?, datetime(\"now\",\"localtime\"))""", entry_tup)
    
    curs.close()
    
    conn.commit()
    
    conn.close()
    
    return


def return_stats(db_path, number = 10):
    
    return_list = []
    
    entry_tup = (number,)
    
    conn = sqlite3.connect(db_path)
    
    curs = conn.cursor()
    
    quer = curs.execute("""select * from scores order by game_number DESC limit ?""", entry_tup)
    
    for items in quer:
        return_list.append(items)
    
    curs.close()
    
    conn.close()
    
    return return_list
    

def return_records(db_path, number = 10, low_to_high = True):
    
    return_list = []
    
    entry_tup = (number,)
    
    conn = sqlite3.connect(db_path)
    
    curs = conn.cursor()
    
    if low_to_high:
        quer = curs.execute("""select * from scores order by score, time_taken limit ?""", entry_tup)
    
    else:
        quer = curs.execute("""select * from scores order by score DESC, time_taken limit ?""", entry_tup)
    
    for items in quer:
        return_list.append(items)
    
    curs.close()
    
    conn.close()
    
    return return_list
