from calendar import Calendar
from datetime import date


# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


day_map = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}
week_map = {"first": 0, "second": 1, "third": 2, "fourth": 3, "fifth": 4}

teenth = {13, 14, 15, 16, 17, 18, 19}


def meetup(year, month, week, day_of_week):
    cal = Calendar()
    dates = []
    for day in cal.itermonthdays(year, month):
        if day == 0:
            continue

        d = date(year, month, day)
        if d.weekday() == day_map[day_of_week]:
            dates.append(day)

    if week == "teenth":
        return date(year, month, teenth.intersection(set(dates)).pop())

    if week == "last":
        return date(year, month, dates.pop())

    try:
        return date(year, month, dates[week_map[week]])
    except IndexError:
        raise MeetupDayException("That day does not exist.")
