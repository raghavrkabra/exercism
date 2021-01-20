"""Solution to Meetup exercise in python track."""

from calendar import Calendar


def meetup(year: int, month: int, week: str, day_of_week: str):
    """Return the date of meetup."""
    days = [day for day in Calendar().itermonthdates(year, month)
            if day.strftime("%A") == day_of_week and day.month == month]
    weeks = {"1st": 0, "2nd": 1, "3rd": 2, "4th": 3, "5th": 4, "last": -1}

    if week == "teenth":
        for day in days:
            if day.day in range(13, 19+1):  # -teen days
                return day

    try:
        return days[weeks[week]]
    except IndexError:
        raise MeetupDayException("No such day exists.")


class MeetupDayException(Exception):
    """MeetupDayException for incorrect parameters in meetup function."""

    pass
