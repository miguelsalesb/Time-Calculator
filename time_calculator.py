def add_time(start, duration, d = ""):

    day = d.lower()

    week_days = {
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
        "sunday": 7
    }
    
    w_day = 0
    final_day = ""
    day_number = 0
    number_of_days = 0

    # Find the position of the colon in order to get the start hour and minutes
    start_colon_position = start.find(":")
    
    # Find the position of the blank space in order to get the period
    start_blank_position = start.find(" ")

    # Find the position of the colon in order to get the duration hour and minutes
    duration_colon_position = duration.find(":")

    start_hour = int(start[:start_colon_position])
    start_minutes = int(start[start_colon_position+1:start_blank_position])

    duration_hour = int(duration[:duration_colon_position])
    duration_minutes = int(duration[duration_colon_position+1:])

    period = start[start_blank_position+1:]

    sum_to_hour = start_hour + duration_hour

    sum_to_minutes = start_minutes + duration_minutes

    if sum_to_hour <= 12:
        final_hour = str(sum_to_hour)
    else :
        # get the hour when it is greater than 24
        final_hour = str(sum_to_hour%12)

    if sum_to_minutes < 60:
        final_minutes = str(sum_to_minutes)
    else:
        # get the minutes if they are greater than 60
        final_minutes = str(sum_to_minutes%60)
        # add an hour if the minutes are greater than 60
        final_hour = str((sum_to_hour%12)+1)
    
    if len(final_minutes) < 2:
        final_minutes = "0" + final_minutes

    # find out how the number of 12 hour periods to get the period
    # if the remainder of the division of the sum of the hours and 12
    number_of_periods = int(sum_to_hour/12)
    
    if period == "AM":
        if sum_to_hour > 12 and sum_to_hour < 24:
            period_final = "PM"
        elif number_of_periods%2 == 0 and sum_to_minutes < 60:
            period_final = "AM"
        else:
            period_final = "PM"
    if period == "PM":
        if sum_to_hour > 12 and sum_to_hour < 24:
            period_final = "AM"
        if number_of_periods%2 == 0 and sum_to_hour > 12:
            period_final = "AM"
        elif number_of_periods%2 == 0 and sum_to_minutes < 60:
            period_final = "PM"
        else:
            period_final = "AM"

    # find out how the number of 24 hour periods
    if sum_to_hour > 24 and sum_to_minutes < 60: 
        number_of_days = round(sum_to_hour/24)
    elif sum_to_hour > 24 and sum_to_minutes > 60: 
        number_of_days = round(sum_to_hour/24) + 1
    else:
        number_of_days = 0
    
    # get the week numeric day
    if len(d) > 0:
        day_number = week_days[day]
        w_day = day_number + number_of_days
    
    if w_day > 7:
        w_day = (day_number + number_of_days) % 7
    
    if w_day == 0:
        w_day = w_day + 1
        
    # get the week day
    for i, v in week_days.items():
        if v == w_day:
            # Change the first letter to uppercase
            final_day = i[0:1].upper() + i[1:]

    if number_of_days == 0 and period == "PM" and period_final == "AM":
        final = " (next day)"
    elif number_of_days < 1 and d != "":
        final = ", " + d
    elif number_of_days == 1 and len(d) == 0:
        final = " (next day)"
    elif number_of_days == 1 and len(d) > 0:
        final = ", " + final_day + " " + "(next day)"
    elif number_of_days > 1 and len(d) == 0:
        final = " (" + str(number_of_days) + " days later)"
    elif number_of_days > 1 and len(d) > 0:
        final = ", " + final_day + " " + "(" + str(number_of_days) + " days later)"
    else:
        final = """"""
    
    new_time = final_hour + ":" + final_minutes + " " + period_final + final

    return new_time