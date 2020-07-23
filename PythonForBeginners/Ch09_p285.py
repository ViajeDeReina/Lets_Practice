# Ch09 > p.285 - Example 2
# Counting & Calculating the data

from time import *
from datetime import *

# Counting the difference between 2 dates, how many days
def countDays(date1, date2):
    day, month, year = date1.split("/")
    sDay = date(int(year), int(month), int(day)) # date 1 saved in sDay
    day, month, year = date2.split("/")
    eDay = date(int(year), int(month), int(day)) # date 2 saved in eDay
    diffDays = eDay - sDay
    retDays = str(diffDays.days)
    return retDays

def getDay(t):
    weeks = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return weeks[t.tm_wday] # it will show you which day depending on the date information

startDate, curDate, tm = "", "", None

if __name__ == "__main__":
    startDate = input("Starting Date(day/month/year) --> ")
    tm = localtime()
    curDate = str(tm.tm_mday)+ "/" + str(tm.tm_mon) + "/" + str(tm.tm_year)
    print("From the date %s till today(%s) has passed %s days."%(startDate, curDate, countDays(startDate,curDate)))
    print("And today is %s."%getDay(tm))