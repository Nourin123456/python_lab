import time,datetime
t=datetime.datetime.now()
print("Date & time:",t)
print("year:",t.year)
print("month:",t.month)
print("weekday:",t.strftime("%A"))
print ("week no:",t.isocalendar()[1])
print("Day of year:",t.timetuple().tm_yday)
print("Day of month:",t.day)
print("Day of week:",time.strftime("%w"))
      
