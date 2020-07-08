"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

user_input = input(
    "select a [month] (##) and [year] (####) seperated by only a comma: ").split(',')

while("" in user_input):
    user_input.remove("")


def is_date_valid(lst):
    if(len(lst) == 1) and lst[0].isdigit():
        if int(lst[0]) > 0 and int(lst[0]) < 13:
            return True
    elif(len(lst) == 2) and lst[0].isdigit() and lst[1].isdigit():
        if int(lst[0]) > 0 and int(lst[0]) < 13 and int(lst[1]) > 0:
            return True
    else:
        return False


if len(user_input) == 0:
    print(calendar.month(datetime.now().year, datetime.now().month))
elif len(user_input) == 1 and is_date_valid(user_input):
    print(calendar.month(datetime.now().year, int(user_input[0])))
elif len(user_input) == 2 and is_date_valid(user_input):
    print(calendar.month(int(user_input[1]), int(user_input[0])))
else:
    print("Please enter an optional month and/or year using numbers only. Seperate month and year by a comma")
    sys.exit()
