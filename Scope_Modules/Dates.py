#PYTHON DATETIME

import datetime

x = datetime.datetime.now()
print(x)

#OUTPUT: 2024-06-18 17:11:00.076811

"""
Date Output

the date contains year,month,day,hour,minute,second,and microsecond.

The datetime module has many methods to return information about the date object.

"""

x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#OUTPUT: 2024
# Tuesday

# The sreftime() method
"""
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string.
"""

x = datetime.datetime(2024,6,18)
print(x.strftime("%B"))
