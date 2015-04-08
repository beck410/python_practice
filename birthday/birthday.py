def days_difference(day1, day2):
    """" (int,inat) -> int
    Return the number of days between day1 and day2, which are both in the range 1-365 (thus indicating the day of the year).
    >>> days_difference(200,244)
    24
    >>> days_difference(50,50)
    0
    >>> days_difference(100,99)
    -1
    """
    return day2-day1


def get_weekday(current_weekday, days_ahead):
    """ (int,int) -> int
    Return which day of the week it will be days_ahead days from current_weekday

    Current weekday is the current day of the week and is in the range 1-7, indicating whether today is Sunday (1), Monday (2), ..., Saturday (7)

    days_ahead is the number of days after tomorrow
    >>> get_weekday(3,1)
    4
    >>> get_weekday(6,1)
    7
    >>> get_weekday(7,1)
    1
    >>> get_weekday(1,0)
    1
    >>> get_weekday(4,7)
    4
    >>> get_weekday(7,72)
    2
    """
    return (current_weekday + days_ahead-1) % 7 + 1


def get_weekday_word(weekday):
    """(int) -> string
    >>> get_weekday_word(1)
    Sunday
    >>> get_weekday_word(5)
    Friday

    Returns the name of the weekday associated with weekday

    weekday is the current day of the week and is in the range 1-7, indicating whether today is Sunday (1) ... Saturday (7).
    """
    return {
            1 : 'Sunday',
            2 : 'Monday',
            3 : 'Tuesday',
            4 : 'Wednesday',
            5 : 'Thursday',
            6 : 'Friday',
            7 : 'Saturday'
    }.get(weekday)


def get_birthday_weekday(current_weekday, current_day,birthday_day):
    """ (int,int) -> string
    >>> get_birthday_weekday(5,3,4)
    Thursday
    >>> get_birthday_weekday(5,3,116)
    Friday
    >>> get_birthday_weekday(6,116,3)
    Friday

    Return the day of the week it will be on birthday_day, given that the day of the week is current_weekday and the day is of the year is current_day

    current_weekday is the current day of the week and is in the range 1-7, indicating whether today is Sunday (1) ... Saturday (7).

    current_day and birthday_day are both in the range 1-365.
    """

    days_diff = days_difference(current_day, birthday_day)
    weekday_num = get_weekday(current_weekday, days_diff)
    return get_weekday_word(weekday_num)


