class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""


time = Time()
time.hour = 7
time.minute = 30
time.second = 56


def increment(time, seconds):
    print ("Original time was: %.2d:%.2d:%.2d"
           % (time.hour, time.minute, time.second))

    time.second += seconds
    if time.second > 59:
        quotient, remainder = divmod(time.second, 60)
        time.minute += quotient
        time.second = remainder
    if time.minute > 59:
        quotient, remainder = divmod(time.minute, 60)
        time.hour += quotient
        time.minute = remainder
    if time.hour > 12:
        time.hour -= 12

    print "Plus %g seconds" % seconds
    print "New time is: %.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)


increment(time, 255)


