from unittest import TestCase

from lasotuvi.Hanh import Hanh


class TestHanh(TestCase):
    def test_KIM(self):
        self.assertEqual(Hanh.KIM.value, 1)

    def test_css_from_hanh(self):
        self.assertEqual(Hanh.KIM.css, 'hanhKim')


    def test_hanh_KIM_short_hand(self):
        self.assertEqual(Hanh.KIM, Hanh.K)

    def test_hanh_cuc(self):
        self.assertEqual(Hanh.KIM.cuc, 4)

    def test_hanh_ten_cuc(self):
        self.assertIn('Kim', Hanh.KIM.ten_cuc)
        self.assertIn('Tứ', Hanh.KIM.ten_cuc)
        self.assertIn('Cục', Hanh.KIM.ten_cuc)