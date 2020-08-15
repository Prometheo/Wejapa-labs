#Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is. For example, calling the function and printing the result like this:

#print(readable_timedelta(10))

#should output the following:

#1 week(s) and 3 day(s).


# write your function here

def readable_timedelta(days):
    weeks = days // 7
    day = days % 7
    suf = lambda p: 's' if p>1 else ''
    return f"{weeks} week{suf(weeks)} and {day} day{suf(day)}"

# test your function
print(readable_timedelta(15))