from unittest import TestCase

from lasotuvi.Hanh import Hanh
from lasotuvi.Sao import Sao, TuVi


class example(Sao):
    id = 1
    ten = 'Tử vi'
    hanh = Hanh.THO
    loai = 2
    phuong_vi = "Đế tinh"
    am_duong = 1
    vong_trang_sinh = 0
    vi_tri_cung = 2


class TestSao(TestCase):
    def test_id(self):
        self.assertEqual(1, example.id)

    def test_ten(self):
        self.assertEqual('Tử vi', example.ten)

    def test_ngu_hanh(self):
        self.assertEqual(Hanh.THO, (example.hanh))

    def test_loai(self):
        self.assertEqual(2, example.loai)
        self.assertEqual(1, TuVi.loai)

    def test_phuong_vi(self):
        self.assertEqual("Đế tinh", example.phuong_vi)

    def test_am_duong(self):
        self.assertEqual(1, example.am_duong)
        self.assertEqual(1, TuVi.am_duong)

    def test_vong_trang_sinh(self):
        self.assertEqual(0, example.vong_trang_sinh)

    def test_dac_tinh(self):
        self.assertTrue(True)

    def test_vi_tri_cung(self):
        self.assertEqual(2, example.vi_tri_cung)
