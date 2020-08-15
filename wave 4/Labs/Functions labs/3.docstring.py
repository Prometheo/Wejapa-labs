def readable_timedelta(days):
    # insert your docstring here
    ''' 
    this is a function that converts integer dates to weeks and days.
    INPUT:
    an integer number that represents days
    OUTPU:
    a pair of two numbers that represents weeks and days.
     '''
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)