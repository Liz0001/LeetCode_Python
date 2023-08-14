from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head.next is None:
            head = None
            return None
        
        count = 0
        middle_step = 0
        middle = head

        while head:
            count += 1
            head = head.next

        head = middle

        while middle:
            middle_step += 1
            if middle_step == count//2:
                if middle.next is None:
                    middle.next = None
                    break
                middle.next = middle.next.next
                break
            middle = middle.next

        return head


class TestSolution(unittest.TestCase):
    """2095. Delete the Middle Node of a Linked List."""

    def test_deleteMiddle(self):
        sol = Solution()
        head = ListNode(1)
        ln2 = ListNode(3)
        ln3 = ListNode(4)
        ln4 = ListNode(7)
        ln5 = ListNode(1)
        ln6 = ListNode(2)
        ln7 = ListNode(6)
        head.next = ln2
        ln2.next = ln3
        ln3.next = ln4
        ln4.next = ln5
        ln5.next = ln6
        ln6.next = ln7
        exp =  [1,3,4,1,2,6]
        out = sol.deleteMiddle(head)
        i = 0
        while out:
            self.assertEqual(out.val, exp[i])
            i+=1
            out = out.next

        head = ListNode(1)
        ln2 = ListNode(2)
        ln3 = ListNode(3)
        ln4 = ListNode(4)
        head.next = ln2
        ln2.next = ln3
        ln3.next = ln4
        exp =  [1,2,4]
        out = sol.deleteMiddle(head)
        i = 0
        while out:
            self.assertEqual(out.val, exp[i])
            i+=1
            out = out.next

        head = ListNode(2)
        ln2 = ListNode(1)
        head.next = ln2
        exp =  [2]
        out = sol.deleteMiddle(head)
        i = 0
        while out:
            self.assertEqual(out.val, exp[i])
            i+=1
            out = out.next

        head = ListNode(1)
        exp =  None
        out = sol.deleteMiddle(head)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
