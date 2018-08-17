from datetime import datetime
from unittest import TestCase

import ephem

from lasotuvi.ErrorHandling import InputInvalidate
from lasotuvi.Lich_EPHEM import is_leap_year, day_in_lunar_year, s2l, find_lunar_day
from lasotuvi.Lich_HND import S2L, jdToDate


class Test_s2l(TestCase):
    def setUp(self):
        self.tunhien = ephem.Observer()
        self.tunhien.lon, self.tunhien.lat = '105.83416', '21.027764'
        self.list_leap_year = [1909, 1862, 1865, 1868, 1871, 1873, 1876, 1879, 1881, 1884, 1887, 1890, 1892,
                               1895, 1898, 1900, 1903, 1906, 1909, 1911, 1917, 1914, 1919, 1922, 1925, 1928, 1930, 1933,
                               1936, 1938, 1941, 1944, 1947, 1949, 1952, 1955, 1957, 1960, 1963, 1966, 1968, 1971, 1974,
                               1976, 1979, 1982, 1985, 1987, 1990, 1993, 1995, 1998, 2001, 2004, 2006, 2009, 2012, 2017,
                               2020, 2023, 2025, 2028, 2031, 2033, 2036, 2039, 2042, 2044]

    def test_is_leap_year(self):
        self.assertRaises(InputInvalidate, day_in_lunar_year, 2001)
        print(day_in_lunar_year('2014'))
        for year in self.list_leap_year:
            year = str(year)
            # print("number of day in %s: %s" % (year, day_in_lunar_year(year)))
            self.assertTrue(is_leap_year(year), '%s is not a leap year' % year)

    def test_2014_paradox(self):
        year = (ephem.Date('2014'))
        prev = ephem.previous_new_moon((ephem.previous_winter_solstice(year)))
        next = ephem.previous_new_moon((ephem.next_winter_solstice(year)))
        # print(prev, next)
        print(next - prev)
        print(ephem.Date("2014/11/22 12:32:16") - ephem.Date("2013/12/3 00:22:23"))

    def test_list_leap_years(self):
        years = range(1860, 2045)
        leap_years = []
        for year in years:
            if is_leap_year(str(year)) == True:
                leap_years.append(year)

        print(set(self.list_leap_year)-set(leap_years))

    def test_s2l_first_test(self):
        testing_time = datetime(1991, 10, 24, 7, 0)
        self.assertEqual(s2l(testing_time, self.tunhien), s2l(testing_time))

    def test_find_lunar_day(self):
        testing_time = datetime(1991, 10, 24, 7, 0)

        self.assertEqual(find_lunar_day(ephem.Date(testing_time)), 17)
