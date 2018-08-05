# -*- coding: utf-8 -*-
"""
(c) 2016 doanguyen <dungnv2410@gmail.com>.
"""

import ephem
from typing import Tuple
from datetime import date

LUNAR_contract = Tuple[date, bool]  # [date, thang_nhuan]


def s2l(solarDate: ephem.Date, location: ephem.Observer, timezone: int) -> LUNAR_contract:
    solarDate += timezone * ephem.hour  # so we are working in the correct timezone

    lunar_leap = False

    previousNewMoon = ephem.previous_new_moon(solarDate)
    lunarDay = solarDate.day - ephem.Date(previousNewMoon).datetime().day + 1

    # Dong chi nam truoc
    previousWinterSolstice = ephem.previous_winter_solstice(solarDate)
    # Dong chi nam sau
    nextWinterSolstice = ephem.next_winter_solstice(solarDate)

    dayInLunarYear = ephem.previous_new_moon(nextWinterSolstice) - ephem.previous_new_moon(previousWinterSolstice)

    diff = int(dayInLunarYear / 29.)

    lunarMonth = diff + 11

    lunarYear = solarDate.year

    if dayInLunarYear > 365:
        lunar_leap = (lunarMonth == find_lunar_month_between(previousWinterSolstice, nextWinterSolstice))

    print(dayInLunarYear, previousWinterSolstice, nextWinterSolstice)
    return tuple(date(lunarYear, lunarMonth, lunarDay), lunar_leap)


def l2s(amlich: LUNAR_contract, location: ephem.Observer) -> LUNAR_contract:
    return amlich, location


def find_new_moon_between(startDate: ephem.Date, endDate: ephem.Date) -> int:
    newMoon = []
    while startDate < endDate:
        newMoon.append(ephem.next_new_moon(startDate))
        startDate += 29.5
    return newMoon


def find_solar_terms_between(startDate: ephem.Date, endDate: ephem.Date) -> list:
    solar_terms = []
    for degree in range(0, 330, 30):
        term = when_is_sun_at_degrees_longitude(startDate, degree)
        if term < endDate:
            solar_terms.append(term)
    return solar_terms


def when_is_sun_at_degrees_longitude(date: date, degrees: int) -> ephem.Date:
    # Thanks to Brandon Rhode @ https://answers.launchpad.net/pyephem/+question/110832

    # Find out the sun's current longitude.

    sun = ephem.Sun(date)
    current_longitude = sun.hlong - ephem.pi

    # Find approximately the right time of year.

    target_longitude = degrees * ephem.degree
    difference = (target_longitude - current_longitude) % ephem.twopi
    t0 = date + 365.25 * difference / ephem.twopi

    # Zero in on the exact moment.

    def f(t):
        sun.compute(t)
        longitude = sun.hlong - ephem.pi
        return ephem.degrees(target_longitude - longitude).znorm

    return ephem.Date(ephem.newton(f, t0, t0 + ephem.minute))
