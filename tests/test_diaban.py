import unittest

import pytest

from lasotuvi.DiaBan import diaBan


@pytest.mark.diaban
class TestDiaBan(unittest.TestCase):
    def test_diaban_is_initializable(self):
       diaban = diaBan(1, 10)
       if diaban:
           self.assertTrue(diaban)
