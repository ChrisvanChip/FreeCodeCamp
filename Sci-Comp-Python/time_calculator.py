# Constants
WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def padding(minutes):
    minutes = str(minutes)
    if len(minutes) == 1:
        minutes = "0" + minutes
    return minutes 

def calc_overload(hours, minutes):
    hours += minutes // 60
    minutes = minutes % 60

    days = hours // 24
    hours = hours % 24

    return days, hours, minutes

def convert_to_24(string):
    is_PM = False
    if string.find("PM") != -1:
        is_PM = True
      
    string = string[:-3]
    hours = int(string.split(":")[0])
    minutes = int(string.split(":")[1])
  
    if is_PM:
        hours += 12
      
    return hours, minutes

def convert_to_12(hours, minutes):
    suffix = " AM"
    if hours >= 12:
        if hours > 12:
            hours -= 12
        suffix = " PM"
      
    if hours == 0:
        hours = 12
      
    return f"{hours}:{padding(minutes)}{suffix}"

def add_time(start, duration, weekday=None):
    # Weekday (optional)
    current_weekday = 0
    if weekday:
        current_weekday = weekdays.index(weekday.lower())

    # Convert AM/PM time string 
    hours, minutes = convert_to_24(start)
    parsed_duration = duration.split(":")
  
    hours += int(parsed_duration[0])
    minutes += int(parsed_duration[1])
    days, hours, minutes = calc_overload(hours, minutes)

    # Amount of days
    days_string = ''
    if days == 1:
        days_string = ' (next day)'
    if days > 1:
        days_string = f' ({days} days later)'

    # Weekday (optional)
    weekday_string = ''
    if weekday:
        current_weekday += days
        current_weekday %= 7
        weekday_string = ', ' + weekdays[current_weekday].title()

    return convert_to_12(hours, minutes) + weekday_string + days_string
