from coverage.backunittest import TestCase

from lasotuvi.lich_HND_JS import *

class TestNewMoon(TestCase):
    def test_decodeLunarYear(self):
        print(decodeLunarYear(11))

    def test_getYearInfo(self):
        print(len(getYearInfo(1993)))
        for info in getYearInfo(1993):
            print(info)

