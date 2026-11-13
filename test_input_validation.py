
from unittest.mock import patch
from inventory_manager import get_positive_float


# Test 1: Valid input
with patch("builtins.input", side_effect=["25"]):
    result = get_positive_float("Enter price: ")
    print("Valid input:", result)


# Test 2: Invalid text followed by valid input
with patch("builtins.input", side_effect=["abc", "30"]):
    result = get_positive_float("Enter price: ")
    print("After invalid text:", result)


# Test 3: Negative number followed by valid input
with patch("builtins.input", side_effect=["-10", "50"]):
    result = get_positive_float("Enter price: ")
    print("After negative input:", result)


# Test 4: Zero followed by valid input
with patch("builtins.input", side_effect=["0", "15"]):
    result = get_positive_float("Enter price: ")
    print("After zero input:", result)
