from unittest import TestCase
from flatmate_class import Flatmate
from bill_class import Bill
from pdf_report_class import PdfReport


class BaseTest(TestCase):
    def setUp(self):
        self.flatmate_x = Flatmate('X', 12)
        self.flatmate_y = Flatmate('Y', 19)
        self.thirty_one_day_month_bill = Bill(100, 31)
        self.pdf_report_z = PdfReport(f'Bill Breakdown: {self.thirty_one_day_month_bill.time_period}')
