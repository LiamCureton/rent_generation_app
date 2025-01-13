from shutil import Error

from flatmate_class import Flatmate
from tests.base_test import BaseTest


class FlatmateTest(BaseTest):
    def test_init(self):
        self.assertEqual(self.flatmate_x.name, 'X')
        self.assertEqual(self.flatmate_y.name, 'Y')
