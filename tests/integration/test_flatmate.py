from tests.base_test import BaseTest


class TestFlatmate(BaseTest):
    def test_pays(self):
        self.assertEqual(self.flatmate_x.pays(self.thirty_one_day_month_bill),38.71)
        self.assertEqual(self.flatmate_y.pays(self.thirty_one_day_month_bill), 61.29)
