import unittest
from src.128_longest_consecutive_sequence import Solution

class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        self.assertEqual(self.solution.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_empty_list(self):
        self.assertEqual(self.solution.longestConsecutive([]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.longestConsecutive([1]), 1)

    def test_no_consecutive_numbers(self):
        self.assertEqual(self.solution.longestConsecutive([1, 3, 5, 7]), 1)

    def test_multiple_consecutive_sequences(self):
        self.assertEqual(self.solution.longestConsecutive([10, 1, 2, 3, 4, 20, 21, 22]), 4)

if __name__ == '__main__':
    unittest.main()