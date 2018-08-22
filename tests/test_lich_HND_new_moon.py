from unittest import TestCase

from ephem import Date

from lasotuvi.Lich_HND import NewMoon, jdToDate, getNewMoonDay, getLunarMonth11, getLeapMonthOffset


class TestNewMoon(TestCase):
    def test_NewMoon(self):
        for x in range(1410, 1425):
            print(jdToDate(getNewMoonDay(x, 7)))
        # for x in range(1, 10):
        #     print("New moon #", x, jdToDate(getNewMoonDay(x, 7)))

    def test_lunar_month_11(self):
        print(jdToDate(getLunarMonth11(2014, 7)), "BRAVO!!! That's the problem!")

    def test_new_moon_in_1993(self):
        for x in range(1150, 1160):
            print(getNewMoonDay(x, 7))
            print(jdToDate(getNewMoonDay(x, 7)))

    def test_getLeapMonthOffset(self):
        jd = 2448981
        print(getLeapMonthOffset(jd, 7))
