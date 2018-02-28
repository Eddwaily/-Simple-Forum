# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet!
# Just brainstorm ways you might approach it!
#                 1  2    3   4   5  6   7   8   9   10  11  12
daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if(year%4==1):return False
    elif(year%100==1):return True
    elif(year%400==1): return False
    else: return True

    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##


def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days=1
    mdays=0
    if(m1==2):
        if(isLeapYear(y1)):mdays=29
        else: mdays=28
    else: mdays=daysOfMonths[m1-1]

    days+=mdays-d1

    while(m1<12):
        m1+=1
        if(m1==2):
            if(isLeapYear(y1)):mdays=29
            else: mdays=28
        else: mdays=daysOfMonths[m1-1]
        days+=mdays
    y1=y1+1

    while(y1<y2):
        if isLeapYear(y1): days+=366
        else: days+=365
        y1+=1

    days+=d2

    i=1
    while(i<m2):
        if i==2:
            if(isLeapYear(y1)):mdays=29
            else: mdays=28
        else: mdays=daysOfMonths[i-1]
        days+=mdays
        i+=1
    return days


print "You are " + str(daysBetweenDates(1996,11,23,2018,2,27)) + " day(s) old !" 
