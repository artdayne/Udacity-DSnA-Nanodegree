def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    
    if day < daysInMonth(year,month):
        return year, month, day+1
    elif month < 12:
        return year, month+1, 1
    else:
        return year+1,1,1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """ Returns True if year1-month1-day1 is before
        year2-month2-day2. Otherwise, returns False. """

    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def isLeapYear(year):
    """ Returns True if the year is a Leap Year
        else, returns False """
    
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    
    return False

def daysInMonth(year, month):
    """ Based on the year and month, returns the
        number of days in the current month """

    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif isLeapYear(year):
        return 29
    else:
        return 28

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    ageInDays = 0

    assert dateIsBefore(year1, month1, day1, year2, month2, day2) 

    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1,month1,day1)
        ageInDays += 1

    return ageInDays

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result == answer and answer != "AssertionError":
                print "Test case passed!"
            else:
                print "Test with data:", args, "failed. You answer was :",result, " when exepcted was:", answer
    
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)

test()
    
