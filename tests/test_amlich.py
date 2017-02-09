from __future__ import absolute_import
import unittest
# from amlich.amlich import jdn


class AmlichTestCase(unittest.TestCase):
    """Tests for `amlich/amlich.py`."""

    def recent_date(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

if __name__ == '__main__':
    unittest.main()
