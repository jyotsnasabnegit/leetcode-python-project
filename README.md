# leetcode-python-project

This project contains solutions to various LeetCode problems implemented in Python. Each problem is organized into its own module within the `src` directory, and corresponding tests are provided in the `tests` directory.

## Project Structure

```
leetcode-python-project
├── src
│   ├── __init__.py
│   ├── 128_longest_consecutive_sequence.py
│   ├── 1_two_sum.py
│   └── 2_add_two_numbers.py
├── tests
│   ├── __init__.py
│   ├── test_128_longest_consecutive_sequence.py
│   ├── test_1_two_sum.py
│   └── test_2_add_two_numbers.py
└── README.md
```

## Problem Descriptions

1. **Longest Consecutive Sequence**: 
   - Implemented in `src/128_longest_consecutive_sequence.py`.
   - The `Solution` class contains the method `longestConsecutive(self, nums)` which returns the length of the longest consecutive elements sequence.

2. **Two Sum**: 
   - Implemented in `src/1_two_sum.py`.
   - The `Solution` class contains the method `twoSum(self, nums, target)` which returns the indices of the two numbers such that they add up to a specific target.

3. **Add Two Numbers**: 
   - Implemented in `src/2_add_two_numbers.py`.
   - The `ListNode` class represents a node in a linked list, and the `Solution` class contains the method `addTwoNumbers(self, l1, l2)` which adds two numbers represented by linked lists and returns the sum as a linked list.

## Running Tests

To run the tests, you can use a testing framework like `unittest` or `pytest`. Navigate to the `tests` directory and run the following command:

```bash
pytest
```

Make sure to have the necessary dependencies installed. You can install them using:

```bash
pip install -r requirements.txt
```