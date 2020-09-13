
m31 = [1, 3, 5, 7, 8, 10, 12]
m30 = [4, 6, 9, 11]

def is_leap_year(year):
    if(year%4 == 0 and (year%100 != 0 or year%400 == 0)):
        return True
    
    else:
        return False
    
def day_in_month(day, month, year):
    if month in m31:
        if day > 31 or day < 1:
            return False
        else:
            return True
    
    elif month in m30:
        if day > 30 or day < 1:
            return False
        else:
            return True
    
    elif month == 2:
        if is_leap_year(year):
            if day > 29 or day < 1:
                return False
            else:
                return True
        
        else:
            if day > 28 or day < 1:
                return False
            else:
                return True
                
    else:
        return False




date_formats = ["DMY", "MDY", "YMD"]

day = 0

month = 0

year = 0

retries = 3

in_format = []

out_format = []

while retries:
    
    in_format = str(input("Please enter an input format for your date (DMY, MDY, YMD): "))

    in_format.strip()

    in_format.upper()

    if in_format in date_formats:
        break
        
    print("Invalid date format.")
    
    retries -= 1

if retries == 0:
    
    print("Aborting program.")
    
    exit()

retries = 3

while retries:
    
    failed = False
    
    date = str(input("Please enter a date: "))

    date.strip()
    
    dmy_tup = date.partition("/")
    
    dmy_tup2 = dmy_tup[2].partition("/")
    
    print(dmy_tup[0], dmy_tup2[0], dmy_tup2[2])
    
    if in_format == "DMY":
        
        
        
        try:
            day = int(dmy_tup[0])
            
        except ValueError as ex:
            print('"%s" cannot be converted to an int: %s' % (dmy_tup[0], ex))
            retries -= 1
            continue
        
        
        try:
            month = int(dmy_tup2[0])
            
        except ValueError as ex:
            print('"%s" cannot be converted to an int: %s' % (dmy_tup2[0], ex))
            retries -= 1
            continue
            
        try:
            year = int(dmy_tup2[2])
            
        except ValueError as ex:
            print('"%s" cannot be converted to an int: %s' % (dmy_tup2[2], ex))
            retries -= 1
            continue
        
        if year < 0:
            print("invalid year")
            retries -= 1
            continue
            
        elif not(month in range(1, 13)):
            print("invalid month")
            retries -= 1
            continue
            
        elif not day_in_month(day, month, year):
            print("Invalid day")
            retries -= 1
            continue
        
        
    elif in_format == "MDY":
        
        
        try:
            day = int(dmy_tup2[0])
            
        except ValueError as ex:
            print('"%s" cannot be converted to an int: %s' % (dmy_tup2[0], ex))
            retries -= 1
            continue
        
        
        try:
            month = int(dmy_tup[0])
            
        except ValueError as ex:
            print('"%s" cannot be converted to an int: %s' % (dmy_tup[0], ex))
            retries -= 1
            continue
            
        try:
            year = int(dmy_tup2[2])
            
        except ValueError as ex:
            print('"%s" cannot be converted to an int: %s' % (dmy_tup2[2], ex))
            retries -= 1
            continue
        
        if year < 0:
            print("invalid year")
            retries -= 1
            continue
            
        elif not(month in range(1, 13)):
            print("invalid month")
            retries -= 1
            continue
            
        elif not day_in_month(day, month, year):
            print("Invalid day")
            retries -= 1
            continue
            
    
    elif in_format == "YMD":
        
        try:
            day = int(dmy_tup2[2])
            
        except ValueError as ex:
            print('"%s" cannot be converted to an int: %s' % (dmy_tup2[2], ex))
            retries -= 1
            continue
        
        
        try:
            month = int(dmy_tup2[0])
            
        except ValueError as ex:
            print('"%s" cannot be converted to an int: %s' % (dmy_tup2[0], ex))
            retries -= 1
            continue
            
        try:
            year = int(dmy_tup[0])
            
        except ValueError as ex:
            print('"%s" cannot be converted to an int: %s' % (dmy_tup[0], ex))
            retries -= 1
            continue
        
        if year < 0:
            print("invalid year")
            retries -= 1
            continue
            
        elif not(month in range(1, 13)):
            print("invalid month")
            retries -= 1
            continue
            
        elif not day_in_month(day, month, year):
            print("Invalid day")
            retries -= 1
            continue
            
    break
        
if retries == 0:
    
    print("Aborting program.")
    
    exit()

retries = 3

while retries:
    
    out_format = str(input("Please enter an output format for your date (DMY, MDY, YMD): "))

    out_format.strip()

    out_format.upper()

    if out_format in date_formats:
        break
        
    print("Invalid date format.")
    
    retries -= 1
    
datelist = [0, 0, 0]

datestr_t = ('','','')

if day < 10:
    datelist[0] = '0'+str(day)
    
else:
    datelist[0] = str(day)
    
if month < 10:
    datelist[1] = '0'+str(month)
    
else:
    datelist[1] = str(month)
    
datelist[2] = str(year)

if out_format == "DMY":
    datestr_t = (datelist[0], datelist[1], datelist[2])
    
elif out_format == "MDY":
    datestr_t = (datelist[1], datelist[0], datelist[2])
    
elif out_format == "YMD":
    datestr_t = (datelist[2], datelist[1], datelist[0])
    

print(f'The date is {datestr_t[0]}/{datestr_t[1]}/{datestr_t[2]}')

