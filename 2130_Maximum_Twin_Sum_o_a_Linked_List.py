from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        heads = []
        max_sum = 0
        
        while head:
            heads.append(head.val)
            head = head.next
        
        j = len(heads)-1
        n = (j+1)//2
        for i in range(n):
            max_sum = max(max_sum, (heads[i]+heads[j]))
            j -= 1
        
        print(max_sum)
        return max_sum


class TestSolution(unittest.TestCase):
    """2130. Maximum Twin Sum of a Linked List."""

    def test_pairSum(self):
        sol = Solution()
        
        n1 = ListNode(5)
        n2 = ListNode(4)
        n3 = ListNode(2)
        n4 = ListNode(1)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        exp = 6
        out = sol.pairSum(n1)
        self.assertEqual(out, exp)

        n1 = ListNode(4)
        n2 = ListNode(2)
        n3 = ListNode(2)
        n4 = ListNode(3)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        exp = 7
        out = sol.pairSum(n1)
        self.assertEqual(out, exp)
        
        n1 = ListNode(1)
        n2 = ListNode(100_000)
        n1.next = n2
        exp = 100001
        out = sol.pairSum(n1)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
