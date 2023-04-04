import unittest
from src.compare import compare


class TestCompare(unittest.TestCase):
    def test_can_compare_3_to_1_retuens_greatee_than(self):
        expected_value = "3 is greater than 1"
        actual_value = compare(3, 1)
        self.assertEqual(expected_value, actual_value)

    def test_comparing_1_to_3_returns_less_than(self):
        expected_value = "1 is less than 3"
        actual_value = compare(1, 3)
        self.assertEqual(expected_value, actual_value)

    def test_comparing_2_to_2_returns_equal(self):
        expected_value = "2 is equal to 2"
        self.assertEqual(expected_value, actual_value)