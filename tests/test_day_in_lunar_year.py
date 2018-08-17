from unittest import TestCase

from lasotuvi.Lich_EPHEM import day_in_lunar_year


class TestDay_in_lunar_year(TestCase):
    def setUp(self):
        self.year_to_test = '1991'

    def test_day_in_lunar_year(self):
        self.assertEqual(353.98237819551287, day_in_lunar_year(self.year_to_test))
        self.assertEqual(383.90005776425096, day_in_lunar_year('2001'))

    def test_day_in_lunar_year_when_the_datetime_over_the_winter_soltice(self):
        self.date_to_test = '2014/12/28 10:10'  # ngày 28/12/2014 quã qua điểm đông chí 22/12/2014
        self.assertEqual(day_in_lunar_year('2014'), day_in_lunar_year(self.date_to_test))

