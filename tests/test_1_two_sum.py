import unittest
from src.1_two_sum import Solution

class TestTwoSum(unittest.TestCase):
    def test_example_case(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_no_solution(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([1, 2, 3], 6), None)

    def test_multiple_solutions(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([3, 2, 4], 6), [1, 2])

    def test_negative_numbers(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([-1, -2, -3, -4, -5], -8), [2, 4])

if __name__ == '__main__':
    unittest.main()