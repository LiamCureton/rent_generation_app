from bill_class import Bill
from tests.base_test import BaseTest

class BillTest(BaseTest):

    def test_init(self):
        self.assertEqual(self.thirty_one_day_month_bill.total, 100)
        self.assertEqual(self.thirty_one_day_month_bill.time_period, 31)
