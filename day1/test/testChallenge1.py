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

if __name__ == "__main__":
    unittest.main()
