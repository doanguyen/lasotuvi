from datetime import datetime
from unittest import TestCase

import ephem

from lasotuvi.ErrorHandling import InputInvalidate
from lasotuvi.Lich_EPHEM import is_leap_year, day_in_lunar_year, s2l, find_lunar_day, find_lunar_month
from lasotuvi.Lich_HND import S2L, jdToDate


class Test_s2l(TestCase):
    def setUp(self):
        self.tunhien = ephem.Observer()
        self.tunhien.lon, self.tunhien.lat = '105.83416', '21.027764'
        self.list_leap_year = [1909, 1862, 1865, 1868, 1871, 1873, 1876, 1879, 1881, 1884, 1887, 1890, 1892,
                               1895, 1898, 1900, 1903, 1906, 1909, 1911, 1917, 1914, 1919, 1922, 1925, 1928, 1930, 1933,
                               1936, 1938, 1941, 1944, 1947, 1949, 1952, 1955, 1957, 1960, 1963, 1966, 1968, 1971, 1974,
                               1976, 1979, 1982, 1985, 1987, 1990, 1993, 1995, 1998, 2001, 2004, 2006, 2009, 2012, 2017,
                               2020, 2023, 2025, 2028, 2031, 2036, 2039, 2042, 2044]

    def test_is_leap_year(self):
        self.assertRaises(InputInvalidate, day_in_lunar_year, 2001)
        for year in self.list_leap_year:
            year = str(year)
            # print("number of day in %s: %s" % (year, day_in_lunar_year(year)))
            self.assertTrue(is_leap_year(year), '%s is not a leap year' % year)

    def test_2014_paradox(self):
        year = (ephem.Date('2014'))
        prev = ephem.previous_new_moon((ephem.previous_winter_solstice(year)))
        next = ephem.previous_new_moon((ephem.next_winter_solstice(year)))
        # self.assertEqual(ephem.Date("2014/11/22 12:32:16"), ephem.Date("2013/12/3 00:22:23"))
        print("Not yet implement")

    def test_list_leap_years(self):
        years = range(1860, 2045)
        leap_years = []
        for year in years:
            if is_leap_year(str(year)) == True:
                leap_years.append(year)

        print(set(self.list_leap_year) - set(leap_years))

    def test_s2l_first_test(self):
        testing_time = datetime(1991, 10, 24, 7, 0)
        timezone = 7
        testing_time = ephem.Date(testing_time)
        lunar_datetime, is_leap = s2l(testing_time, timezone)
        print(ephem.Date(lunar_datetime).triple())

    def test_s2l_hanh_birth_day(self):
        testing_time = datetime(1993, 8, 7, 12, 0)
        timezone = 7
        testing_time = ephem.Date(testing_time)
        lunar_datetime, is_leap = s2l(testing_time, timezone)
        print(ephem.Date(lunar_datetime), is_leap)

    def test_find_lunar_day(self):
        testing_time = datetime(1991, 10, 24, 7, 0)

        lunar_day = find_lunar_day(ephem.Date(testing_time), 7)
        self.assertEqual(lunar_day, 17)

    def test_find_lunar_day_with_wrong_timezone(self):
        # TODO: what's wrong here!
        testing_time = ephem.Date(datetime(1991, 10, 24, 7, 0))
        wrong_timezone = 0
        correct_timezone = 7
        lunar_day = find_lunar_day(testing_time, wrong_timezone)
        self.assertNotEqual(lunar_day, find_lunar_day(testing_time, correct_timezone))

    def test_find_lunar_day_ephem_date(self):
        testing_time = ephem.Date(datetime(1991, 10, 24, 7, 0))
        correct_timezone = 7
        find_lunar_day(testing_time, correct_timezone)

    # def test_is_leap_month(self):
    def test_find_lunar_month(self):
        testing_time = ephem.Date(datetime(2014, 2, 1, 7, 0))
        timzone = 7
        self.assertEqual(find_lunar_month(testing_time, timzone), (1, False))

    def test_find_lunar_month_1990_leap_month(self):
        testing_time = ephem.Date(datetime(1990, 5, 10, 10, 0))
        timezone = 7
        print(find_lunar_month(testing_time, timezone))

    def test_find_lunar_month_2017_leap_month(self):
        testing_time, timezone = ephem.Date(datetime(2017, 2, 10, 10, 0)), 7
        print(find_lunar_month(testing_time, timezone))

    def test_find_lunar_month_of_leap_year(self):
        testing_time, timezone = ephem.Date(datetime(2006, 8, 28, 10, 0)), 7
        self.assertEqual(find_lunar_month(testing_time, timezone), (7, True))

    def test_find_lunar_month_from_1990_to_2012(self):
        solar_dates = [(year, month, day) for year in range(1990, 2012) for month in range(1, 12) for day in (1, 28)]
        for instance in solar_dates:
            solar_date = ephem.Date(datetime(instance[0], instance[1], instance[2]))
            # lunar_month = s2l(solar_date, 7)
            lunar_month_expected = S2L(instance[2], instance[1], instance[0])[1]
            lunar_month = find_lunar_month(ephem.Date(solar_date))
            if instance[0] != 1993 and not (instance[0] == 1995 and instance[1] == 1 and instance[2] == 1):
                print("Converting date", solar_date)
                self.assertEqual(lunar_month[0], lunar_month_expected,
                                 "Datetime %s:\n  Our calculation: %s is not match with\n HND calculation: %s" % (
                                     solar_date, lunar_month, lunar_month_expected))

    def test_find_lunar_month_1993_04_28(self):
        solar_date = ephem.Date('1993/4/28 00:00:00')
        # print(ephem.previous_new_moon(ephem.previous_winter_solstice(solar_date)))
        self.assertEqual(find_lunar_month(solar_date, 7), (3, True))

    def test_is_leap_year_1993_04_28(self):
        solar_date = ephem.Date('1993/4/28 00:00:00')
        self.assertTrue(is_leap_year(solar_date))
        year_1989 = ephem.Date('1989/2/10')
        self.assertFalse(is_leap_year(year_1989))
        year_1990 = ephem.Date('1990/10/5')
        self.assertTrue(is_leap_year(year_1990))

    def test_is_leap_year_2019(self):
        solar_date = ephem.Date('2019/02/10')
        self.assertFalse(is_leap_year(solar_date))

    def test_compare_pyephem_vs_nasa(self):
        solar_date = ephem.Date('2018/9/11')
        print(ephem.previous_new_moon(solar_date))
