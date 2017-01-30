from lasotuvi.src.AmDuong import *
from lasotuvi.src.lichamduong import *
import unittest


class TestLichAmDuong(unittest.TestCase):

    def test_my(self):
        self.assertEqual('foo'.upper(), "FOO")


def main():
    unittest.main()

if __name__ == '__main__':
    main()
