from datetime import date
import calendar

class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message


def meetup(year, month, week, weekday):
    # Map English weekday names to calendar module integers (Monday=0, Sunday=6)
    weekday_map = {
        "Monday": calendar.MONDAY,
        "Tuesday": calendar.TUESDAY,
        "Wednesday": calendar.WEDNESDAY,
        "Thursday": calendar.THURSDAY,
        "Friday": calendar.FRIDAY,
        "Saturday": calendar.SATURDAY,
        "Sunday": calendar.SUNDAY
    }
    
    target_weekday = weekday_map[weekday]
    
    # Generate a matrix representing the month's calendar
    # calendar.monthcalendar returns lists of 7 days, where 0 means the day belongs to another month
    month_cal = calendar.monthcalendar(year, month)
    
    # Extract all real days of the month that fall on our target weekday
    matching_days = []
    for week_list in month_cal:
        day = week_list[target_weekday]
        if day != 0:
            matching_days.append(day)
            
    # Handle the lookup based on the specific week descriptor
    try:
        if week == "first":
            day = matching_days[0]
        elif week == "second":
            day = matching_days[1]
        elif week == "third":
            day = matching_days[2]
        elif week == "fourth":
            day = matching_days[3]
        elif week == "fifth":
            # If the list is too short, indexing will throw an IndexError, which we catch below
            day = matching_days[4]
        elif week == "last":
            day = matching_days[-1]
        elif week == "teenth":
            # Filter the list to find the one day falling between 13 and 19 inclusive
            teenth_days = [d for d in matching_days if 13 <= d <= 19]
            day = teenth_days[0]
        else:
            raise MeetupDayException("Invalid week descriptor.")
            
    except (IndexError, KeyError):
        raise MeetupDayException("That day does not exist.")

    return date(year, month, day)