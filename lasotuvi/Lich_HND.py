"""
(c) 2006 Ho Ngoc Duc.
Astronomical algorithms
from the book "Astronomical Algorithms" by Jean Meeus, 1998
"""

import math


def jdFromDate(dd, mm, yy):
    '''def jdFromDate(dd, mm, yy): Compute the (integral) Julian day number of
    day dd/mm/yyyy, i.e., the number of days between 1/1/4713 BC
    (Julian calendar) and dd/mm/yyyy.'''
    a = int((14 - mm) / 12.)
    y = yy + 4800 - a
    m = mm + 12 * a - 3
    jd = dd + int((153 * m + 2) / 5.) \
        + 365 * y + int(y / 4.) - int(y / 100.) \
        + int(y / 400.) - 32045
    if (jd < 2299161):
        jd = dd + int((153 * m + 2) / 5.) \
            + 365 * y + int(y / 4.) - 32083
    return jd


def jdToDate(jd):
    '''def jdToDate(jd): Convert a Julian day number to day/month/year.
                       jd is an integer.'''
    if (jd > 2299160):
        # After 5/10/1582, Gregorian calendar
        a = jd + 32044
        b = int((4 * a + 3) / 146097.)
        c = a - int((b * 146097) / 4.)
    else:
        b = 0
        c = jd + 32082
    d = int((4 * c + 3) / 1461.)
    e = c - int((1461 * d) / 4.)
    m = int((5 * e + 2) / 153.)
    day = e - int((153 * m + 2) / 5.) + 1
    month = m + 3 - 12 * int(m / 10.)
    year = b * 100 + d - 4800 + int(m / 10.)
    return [day, month, year]


def NewMoon(k):
    '''def NewMoon(k): Compute the time of the k-th new moon after
    the new moon of 1/1/1900 13:52 UCT (measured as the number of
    days since 1/1/4713 BC noon UCT, e.g., 2451545.125 is 1/1/2000 15:00 UTC.
    Returns a floating number, e.g., 2415079.9758617813 for k=2 or
    2414961.935157746 for k=-2.'''
    # Time in Julian centuries from 1900 January 0.5
    T = k / 1236.85
    T2 = T * T
    T3 = T2 * T
    dr = math.pi / 180.
    Jd1 = 2415020.75933 + 29.53058868 * k \
        + 0.0001178 * T2 - 0.000000155 * T3
    Jd1 = Jd1 + 0.00033 * math.sin(
        (166.56 + 132.87 * T - 0.009173 * T2) * dr)
    # Mean new moon
    M = 359.2242 + 29.10535608 * k \
        - 0.0000333 * T2 - 0.00000347 * T3
    # Sun's mean anomaly
    Mpr = 306.0253 + 385.81691806 * k \
        + 0.0107306 * T2 + 0.00001236 * T3
    # Moon's mean anomaly
    F = 21.2964 + 390.67050646 * k - 0.0016528 * T2 \
        - 0.00000239 * T3
    # Moon's argument of latitude
    C1 = (0.1734 - 0.000393 * T) * math.sin(M * dr) \
        + 0.0021 * math.sin(2 * dr * M)
    C1 = C1 - 0.4068 * math.sin(Mpr * dr) \
        + 0.0161 * math.sin(dr * 2 * Mpr)
    C1 = C1 - 0.0004 * math.sin(dr * 3 * Mpr)
    C1 = C1 + 0.0104 * math.sin(dr * 2 * F) \
        - 0.0051 * math.sin(dr * (M + Mpr))
    C1 = C1 - 0.0074 * math.sin(dr * (M - Mpr)) \
        + 0.0004 * math.sin(dr * (2 * F + M))
    C1 = C1 - 0.0004 * math.sin(dr * (2 * F - M)) \
        - 0.0006 * math.sin(dr * (2 * F + Mpr))
    C1 = C1 + 0.0010 * math.sin(dr * (2 * F - Mpr)) \
        + 0.0005 * math.sin(dr * (2 * Mpr + M))
    if (T < -11):
        deltat = 0.001 + 0.000839 * T + 0.0002261 * T2 \
            - 0.00000845 * T3 - 0.000000081 * T * T3
    else:
        deltat = -0.000278 + 0.000265 * T + 0.000262 * T2
    JdNew = Jd1 + C1 - deltat
    return JdNew


def SunLongitude(jdn):
    '''def SunLongitude(jdn): Compute the longitude of the sun at any time.
    Parameter: floating number jdn, the number of days since 1/1/4713 BC noon.
    '''
    T = (jdn - 2451545.0) / 36525.
    # Time in Julian centuries
    # from 2000-01-01 12:00:00 GMT
    T2 = T * T
    dr = math.pi / 180.  # degree to radian
    M = 357.52910 + 35999.05030 * T \
        - 0.0001559 * T2 - 0.00000048 * T * T2
    # mean anomaly, degree
    L0 = 280.46645 + 36000.76983 * T + 0.0003032 * T2
    # mean longitude, degree
    DL = (1.914600 - 0.004817 * T - 0.000014 * T2) \
        * math.sin(dr * M)
    DL += (0.019993 - 0.000101 * T) * math.sin(dr * 2 * M) \
        + 0.000290 * math.sin(dr * 3 * M)
    L = L0 + DL  # true longitude, degree
    L = L * dr
    L = L - math.pi * 2 * (float(L / (math.pi * 2)))
    # Normalize to (0, 2*math.pi)
    return L


def getSunLongitude_OLD(dayNumber, timeZone):
    '''def getSunLongitude(dayNumber, timeZone):
Compute sun position at midnight of the day with the given Julian day number.
The time zone if the time difference between local time, UTC: 7.0 for UTC+7:00

The function returns a number between 0 and 11. From the day after March
equinox and the 1st major term after March equinox, 0 is returned.
After that, return 1, 2, 3 ...'''
    return int(
        SunLongitude(dayNumber - 0.5 - timeZone / 24.) / math.pi * 6)


def getSunLongitude(jdn, timeZone):
    T = (jdn - 2451545.5 - timeZone/24.) / 36525.
    T2 = T**2
    dr = math.pi / 180.
    M = 357.52910 + 35999.05030*T - 0.0001559*T2 - 0.00000048*T*T2
    L0 = 280.46645 + 36000.76983*T + 0.0003032*T2
    DL = (1.914600 - 0.004817*T - 0.000014*T2)*math.sin(dr*M)
    DL = DL + (0.019993 - 0.000101*T)*math.sin(dr*2*M) + 0.000290*math.sin(dr*3*M)
    L = L0 + DL
    omega = 125.04 - 1934.136 * T
    L = L - 0.00569 - 0.00478 * math.sin(omega * dr)
    L = L*dr
    L = L - math.pi*2*(math.floor(L/(math.pi*2)))
    return int(L/math.pi*6)


def getNewMoonDay(k, timeZone):
    '''def getNewMoonDay(k, timeZone): Compute the day of the k-th new moon
    in the given time zone. The time zone if the time difference between local
    time and UTC: 7.0 for UTC+7:00.'''
    return int(NewMoon(k) + 0.5 + timeZone / 24.)


def getLunarMonth11(yy, timeZone):
    '''def getLunarMonth11(yy, timeZone):  Find the day that starts the luner month
    11of the given year for the given time zone.'''
    # off = jdFromDate(31, 12, yy) \
    #            - 2415021.076998695
    off = jdFromDate(31, 12, yy) - 2415021.
    k = int(off / 29.530588853)
    nm = getNewMoonDay(k, timeZone)
    sunLong = getSunLongitude(nm, timeZone)
    # sun longitude at local midnight
    if (sunLong >= 9):
        nm = getNewMoonDay(k - 1, timeZone)
    return nm

# print getLunarMonth11(1992, 7)
def getLeapMonthOffset(a11, timeZone):
    '''def getLeapMonthOffset(a11, timeZone): Find the index of the leap month
    after the month starting on the day a11.'''
    k = int((a11 - 2415021.076998695) / 29.530588853 + 0.5)
    last = 0
    i = 1  # start with month following lunar month 11
    arc = getSunLongitude(
        getNewMoonDay(k + i, timeZone), timeZone)
    while True:
        last = arc
        i += 1
        arc = getSunLongitude(
            getNewMoonDay(k + i, timeZone),
            timeZone)
        if not (arc != last and i < 14):
            break
    return i - 1


def S2L(dd, mm, yy, timeZone=7):
    '''def S2L(dd, mm, yy, timeZone = 7): Convert solar date dd/mm/yyyy to
    the corresponding lunar date.'''
    dayNumber = jdFromDate(dd, mm, yy)
    k = int((dayNumber - 2415021.076998695) / 29.530588853)
    monthStart = getNewMoonDay(k + 1, timeZone)
    if (monthStart > dayNumber):
        monthStart = getNewMoonDay(k, timeZone)
    # alert(dayNumber + " -> " + monthStart)
    a11 = getLunarMonth11(yy, timeZone)
    b11 = a11
    if (a11 >= monthStart):
        lunarYear = yy
        a11 = getLunarMonth11(yy - 1, timeZone)
    else:
        lunarYear = yy + 1
        b11 = getLunarMonth11(yy + 1, timeZone)
    lunarDay = dayNumber - monthStart + 1
    diff = int((monthStart - a11) / 29.)

    lunarLeap = 0
    lunarMonth = diff + 11

    if (b11 - a11 > 365):
        leapMonthDiff = \
            getLeapMonthOffset(a11, timeZone)
        if (diff >= leapMonthDiff):
            lunarMonth = diff + 10
            if (diff == leapMonthDiff):
                lunarLeap = 1
    if (lunarMonth > 12):
        lunarMonth = lunarMonth - 12
    if (lunarMonth >= 11 and diff < 4):
        lunarYear -= 1
    # print [lunarDay, lunarMonth, lunarYear, lunarLeap]
    return \
        [lunarDay, lunarMonth, lunarYear, lunarLeap]


def L2S(lunarD, lunarM, lunarY, lunarLeap, tZ=7):
    '''def L2S(lunarD, lunarM, lunarY, lunarLeap, tZ = 7): Convert a lunar date
    to the corresponding solar date.'''
    if (lunarM < 11):
        a11 = getLunarMonth11(lunarY - 1, tZ)
        b11 = getLunarMonth11(lunarY, tZ)
    else:
        a11 = getLunarMonth11(lunarY, tZ)
        b11 = getLunarMonth11(lunarY + 1, tZ)
    k = int(0.5 +
            (a11 - 2415021.076998695) / 29.530588853)
    off = lunarM - 11
    if (off < 0):
        off += 12
    if (b11 - a11 > 365):
        leapOff = getLeapMonthOffset(a11, tZ)
        leapM = leapOff - 2
        if (leapM < 0):
            leapM += 12
        if (lunarLeap != 0 and lunarM != leapM):
            return [0, 0, 0]
        elif (lunarLeap != 0 or off >= leapOff):
            off += 1
    monthStart = getNewMoonDay(k + off, tZ)
    return jdToDate(monthStart + lunarD - 1)
