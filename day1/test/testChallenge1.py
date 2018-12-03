#! /usr/bin/env python3

import unittest
import challenge1

class TestChallenge1Methods(unittest.TestCase):

    def test_add_string_to_total(self):
        """
        Test that function that updates the total works correctly
        """
        result = 300
        current = 0
        value = "+300"
        self.assertEqual(result, challenge1.add_to_frequency(current, value), "Values don't match")

    def test_minus_string_from_total(self):
        """
        Test that function that updates the total works correctly
        """
        result = 100
        current = 120
        value = "-20"
        self.assertEqual(result, challenge1.add_to_frequency(current, value), "Values don't match")

    def test_frequency_total(self):
        values = ["+100", "-50", "+1", "-9"]
        result = 42
        self.assertEqual(result, challenge1.find_final_frequency(values), "Frequency counting failed")

if __name__ == "__main__":
    unittest.main()
