from tests.base_test import BaseTest
from pdf_report_class import PdfReport

class PdfTest(BaseTest):
    def test_init(self):
        self.assertEqual(self.pdf_report_z.filename, 'Bill Breakdown: 31')