import unittest
from unittest.mock import patch

from inventory_manager import get_positive_float


class TestPositiveFloatInput(unittest.TestCase):

    @patch("builtins.input", side_effect=["25"])
    def test_valid_input(self, mock_input):
        self.assertEqual(get_positive_float("Price: "), 25.0)

    @patch("builtins.input", side_effect=["abc", "30"])
    def test_invalid_text_then_valid_input(self, mock_input):
        self.assertEqual(get_positive_float("Price: "), 30.0)

    @patch("builtins.input", side_effect=["-10", "50"])
    def test_negative_then_valid_input(self, mock_input):
        self.assertEqual(get_positive_float("Price: "), 50.0)

    @patch("builtins.input", side_effect=["0", "15"])
    def test_zero_then_valid_input(self, mock_input):
        self.assertEqual(get_positive_float("Price: "), 15.0)


if __name__ == "__main__":
    unittest.main()
