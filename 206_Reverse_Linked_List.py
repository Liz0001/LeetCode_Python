from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        new_head = None

        if head is None:
            return head

        if head.next is None:
            return head

        while head:
            next_one = head.next
            head.next = new_head
            
            new_head = head
            head = next_one

        return new_head
    

class TestSolution(unittest.TestCase):
    """206. Reverse Linked List."""

    def test_reverseList(self):
        sol = Solution()

        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n4 = ListNode(4)
        n5 = ListNode(5)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5

        exp = [5,4,3,2,1]
        out = sol.reverseList(n1)

        reversed_list = []
        while out:
            reversed_list.append(out.val)
            out = out.next

        self.assertEqual(reversed_list, exp)


        n1 = ListNode(1)
        n2 = ListNode(2)
        n1.next = n2

        exp = [2,1]
        out = sol.reverseList(n1)

        reversed_list = []
        while out:
            reversed_list.append(out.val)
            out = out.next

        self.assertEqual(reversed_list, exp)


        exp = None
        out = sol.reverseList(None)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
