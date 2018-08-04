import unittest

import pytest

from lasotuvi.DiaBan import cungDiaBan


@pytest.mark.diaban
class TestDiaBan(unittest.TestCase):
    def test_diaban_is_initializable(self):
       diaban = cungDiaBan(1)
       if diaban:
           self.assertTrue(diaban)
