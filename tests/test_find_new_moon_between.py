from unittest import TestCase

from ephem import Date


class TestFind_new_moon_between(TestCase):

    def test_find_new_moon_between_year_1993_1994(self):
        """
        Context: The month from 28/11 16:41 to 27/01 02:20 is longer than 29.5 days, so in the calculation,
        new moon at 28/11 16:41 apprear twice
        """
        start_date = Date('1989/12/28 10:20')
        end_date = Date('1990/01/27 02:20')
        self.assertFalse(end_date - start_date < 29.5)
