import datetime
from calendar import Calendar


def meetup(year: int, month: int, week: str, day_of_week: str):
    cal = Calendar()
    days = [day for day in cal.itermonthdates(year, month)
            if day.strftime("%A") == day_of_week and day.month == month]
    weeks = {"1st":0, "2nd":1, "3rd":2, "4th":3, "5th":4, "last":-1}

    if week == "teenth":
        for day in days:
            if day.day in range(13, 19+1):
                return day
    try:
        return days[weeks[week]]
    except IndexError:
        raise MeetupDayException("day does not exist")

def MeetupDayException(Exception):
    pass
