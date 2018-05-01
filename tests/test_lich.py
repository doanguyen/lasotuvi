from __future__ import absolute_import

from datetime import date

import pytest
from ephem import Date, Observer

from src.Lich import S2L, find_solar_terms_between, when_is_sun_at_degrees_longitude, find_new_moon_between
from src.lich_bak import S2L as S2L_bak
from src.lich_bak import jdFromDate, jdToDate

calendar_table = {
    date(1991, 10, 24): (date(1991, 9, 17), False),
    date(1987, 8, 29): (date(1987, 7, 6), True),
}


@pytest.mark.lich
class TestLich(object):

    def setup_method(self):
        self.tunhien = Observer()
        self.tunhien.lon, self.tunhien.lat = '105.83416', '21.027764'
        self.timezone = 7
        self.solardate = date(1991, 10, 24)

    @pytest.mark.s2l
    def test_S2L(self):
        self.lunardate = S2L(self.solardate, self.tunhien, self.timezone)
        for solar, lunar in calendar_table.items():
            assert lunar == S2L(solar, self.tunhien, self.timezone)

    @pytest.mark.justtest
    def test_S2L2(self):
        S2L_bak(24, 10, 1991)
        S2L(self.solardate, self.tunhien, self.timezone)
        assert False
    
    @pytest.mark.findsolarterms
    def test_find_solar_terms_between(self):
        startDate = Date("1983/12/1")
        endDate = Date('1984/12/23')
        terms = find_solar_terms_between(startDate, endDate)
        for x in terms:
            print(Date(x))
        assert False
    
    @pytest.mark.degrees
    def test_when_sun_is_at_degree(self):
        startDate = Date('1983/12/1')
        print(when_is_sun_at_degrees_longitude(startDate, 0))
        assert False
    
    @pytest.mark.findnewmoon
    def test_new_moon_list(self):
        startDate = Date('1983/12/1')
        endDate = Date('1984/12/23')

        newmoons = find_new_moon_between(startDate, endDate)

        for newmoon in newmoons:
            print(newmoon)
        
        assert False