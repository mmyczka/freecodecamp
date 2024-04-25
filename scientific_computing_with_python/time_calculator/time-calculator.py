def add_time(start, duration, starting_day=None):
   
    # Convert times to minutes
    start_to_minutes = time_to_minutes(start)
    duration_to_minutes = time_to_minutes(duration)
    sum_of_times = start_to_minutes + duration_to_minutes

    # Calculate number of days and time from minutes 
    days, remaining_minutes = divmod(sum_of_times, 24*60)
    hours, minutes = divmod(remaining_minutes, 60)

    # Convert time to AM/PM
    time = convert_to_AM_PM(hours, minutes)

    # Get the day name
    day_name = ""
    if starting_day:
        day_name = ", " + get_day_name(starting_day.capitalize(), days) 

    # Get number of day ending
    days_result = ""
    if days == 1:
        days_result = ' (next day)'
    elif days > 1:
        days_result = f' ({days} days later)'

    return time + day_name + days_result

def time_to_minutes(time):
    elements = time.split()
    hours, minutes = map(int, elements[0].split(':'))

    if len(elements) == 2:
        if elements[1] == 'PM' and hours != 12:
            hours += 12
        elif elements[1] == 'AM' and hours == 12:
            hours = 0

    return hours * 60 + minutes

def convert_to_AM_PM(hours, minutes):
    if hours == 0:
        return '12:{:02d} AM'.format(minutes)
    elif hours == 12:
        return '12:{:02d} PM'.format(minutes)
    elif hours > 12:
        return'{:d}:{:02d} PM'.format(hours - 12, minutes)
    else:
        return '{:d}:{:02d} AM'.format(hours, minutes)

def get_day_name(start_day, days):
    days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    start_index = days_list.index(start_day)
    day_index = (start_index + days) % 7

    return days_list[day_index]


print(add_time('8:16 PM', '466:02', 'tuesday'))