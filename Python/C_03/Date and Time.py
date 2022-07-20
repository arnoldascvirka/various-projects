########################
#   Usage of From (Module) import (Foo)
########################

# from datetime import datetime
# from datetime import date


# today =  datetime.today()
# print(today)

# today2 = date.today()
# print(today2)

# print("Data type: ", type((today)))

########################
#   Usage of Import (Module) and change time
########################

# import datetime

# print("Type Date-Time, only use different parameters: ")
# datetime1 = datetime.datetime(2022, 12, 31, 0, 45, 10)
# print(datetime1)

# from datetime import datetime
# formated = datetime.strftime("%A, %d")

########################
#   Usage of datetime (timedelta)
########################

import datetime
from multiprocessing.spawn import import_main_path
from this import d

now = datetime.datetime.now()
print(now)
print("Data type: ", type(now))
print("Using timedelta days - day time difference")
difference = datetime.timedelta(days=2)
print(now - difference)
print(now + difference)
print("Using timedelta hours - day hour difference")
difference = datetime.timedelta(hours=100)
print(now - difference)
print(now + difference)
print("Using timedelta hour and days")
difference = datetime.timedelta(days=2, hours=5)
print(now - difference)
print(now + difference)
print("Using timedelta full, r")
difference = datetime.timedelta(days=1, hours=5, minutes=20, seconds=50) 

########################
#   Usage of input time
########################

print("Get formatting from user for date")
input1 = input("Type date in YYYY-MM-DD HH.MM.SS format: ")
date = datetime.datetime.strptime(input1, "%Y-%m-%d %H:%M:%S")
print(type(date))
print("Calculates the difference between 2 dates")
diff = datetime.datetime.now() - date
print("In the difference, we get the data type: ", type(diff))
print("The difference between two days is: ", diff)

