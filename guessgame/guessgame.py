# guessgame.py - an example game to demonstrate usage of the "scoredb" module

import random as r
import time
import scoredb as sdb

db_path = ""

def guessing_game():
    print("Please enter your name:")
    
    name = input();
    
    print("Guess the number between 1 and 100! Type \"0\" to quit.")
    
    secret_no = r.randint(1, 100)
    
    guesscount = 0;
    
    starttime = time.time()
    
    while 1:
        print("Take a guess:")
        
        try:
            guess = int(input(""))
            if not guess:
                break
        except ValueError:
            print("Not an integer, try again!")
            continue
        
        guesscount += 1
        
        if guess < secret_no :
            print("Too low!")
            
        elif guess > secret_no :
            print("Too high!")
            
        else:
            endtime = time.time()
            time_taken = endtime - starttime
            
            dummystring = " guess and " if guesscount == 1 else " guesses and "
            print("Congratulations! You guessed it in "+str(guesscount)+dummystring+str(time_taken)+" seconds!")
            
            sdb.add_score_to_db(name, guesscount, time_taken, db_path)
            break
    
    return


def display_help():
    print("\nCalling without arguments equivalent to passing option \"-play\"\n")
    
    print("-help -- show help\n")
    
    print("-stats [number] -- display all games played from most recent to oldest")
    
    print("If number is not given, displays 10 results\n")
    
    print("-records [number] -- displays all games played in order of score")
    
    print("If number is not given, displays 10 results\n")
    
    print("-play -- start a guessing game\n")
    
    print("Arguments after the first are ignored.\n")
    
    return


arglist = ["-help", "-stats", "-records", "-play"]

if __name__ == "__main__":
    import sys as s 
    
    db_path = s.argv[0][0:len(s.argv[0]) - 2]+"db"
    
    results = []
    
    if len(s.argv) == 1:
        guessing_game()
    
    elif not s.argv[1] in arglist:
        print("Invalid Argument - use \"-help\" for more options.")
    
    elif s.argv[1] == "-play":
        guessing_game()
        
    elif s.argv[1] == "-help":
        display_help()
    
    elif s.argv[1] == "-stats":
        try:
            number = int(s.argv[2])
            results = sdb.return_stats(db_path, number)
            
        except (ValueError, IndexError):
            results = sdb.return_stats(db_path)
            
        for stuff in results:
            print(stuff)
    
    
    elif s.argv[1] == "-records":
        try:
            number = int(s.argv[2])
            results = sdb.return_records(db_path, number)
            
        except (ValueError, IndexError):
            results = sdb.return_records(db_path)
        
        for stuff in results:
            print(stuff)
            
    exit()

