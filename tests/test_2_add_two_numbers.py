import unittest
from src.2_add_two_numbers import Solution, ListNode

class TestAddTwoNumbers(unittest.TestCase):
    def list_to_linkedlist(self, lst):
        head = ListNode(0)
        current = head
        for number in lst:
            current.next = ListNode(number)
            current = current.next
        return head.next

    def linkedlist_to_list(self, node):
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    def test_add_two_numbers(self):
        solution = Solution()

        # Test case 1
        l1 = self.list_to_linkedlist([2, 4, 3])
        l2 = self.list_to_linkedlist([5, 6, 4])
        result = solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linkedlist_to_list(result), [7, 0, 8])

        # Test case 2
        l1 = self.list_to_linkedlist([0])
        l2 = self.list_to_linkedlist([0])
        result = solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linkedlist_to_list(result), [0])

        # Test case 3
        l1 = self.list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
        l2 = self.list_to_linkedlist([9, 9, 9, 9])
        result = solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linkedlist_to_list(result), [8, 9, 9, 9, 0, 0, 0, 1])

if __name__ == '__main__':
    unittest.main()