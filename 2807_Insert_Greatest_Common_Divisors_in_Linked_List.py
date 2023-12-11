import unittest
from math import lcm


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: [ListNode]) -> [ListNode]:
        curr = head
        ptr = head.next
        while ptr:
            gcd =  int((curr.val * ptr.val)/ lcm(curr.val, ptr.val))
            node = ListNode(gcd)
            node.next = ptr
            curr.next = node
            curr = ptr
            ptr = ptr.next
            
        return head


class TestSolution(unittest.TestCase):
    """2807. Insert Greatest Common Divisors in Linked List."""

    def test_insertGreatestCommonDivisors(self):
        sol = Solution()
        
        values = [18,6,10,3]
        head = curr = ListNode(values[0])
        
        for i in range(1, len(values)):
            curr.next = ListNode(values[i])
            curr = curr.next
        
        exp = [18,6,6,2,10,1,3]
        out = sol.insertGreatestCommonDivisors(head)
        out_vals = []
        while out:
            out_vals.append(out.val)
            out = out.next
        self.assertEqual(out_vals, exp)
        
        
        values = [7]
        head = curr = ListNode(values[0])
        
        for i in range(1, len(values)):
            curr.next = ListNode(values[i])
            curr = curr.next
        
        exp = [7]
        out = sol.insertGreatestCommonDivisors(head)
        out_vals = []
        while out:
            out_vals.append(out.val)
            out = out.next
        self.assertEqual(out_vals, exp)


if __name__ == '__main__':
    unittest.main()
