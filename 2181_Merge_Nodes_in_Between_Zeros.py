import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    
class Solution:
    def mergeNodes(self, head: [ListNode]) -> [ListNode]:
        curr = new_head = ListNode()
        head = head.next
        t = 0
        while head:
            if head.val == 0:
                curr.next = ListNode(t)
                curr = curr.next
                t = 0   
            else:
                t += head.val   
            head = head.next
    
        return new_head.next


class TestSolution(unittest.TestCase):
    """2181. Merge Nodes in Between Zeros."""

    def test_mergeNodes(self):
        sol = Solution()

        exp = [4,11]
        curr = head = ListNode(0)
        for i in [3,1,0,4,5,2,0]:
            curr.next = ListNode(i)
            curr = curr.next
        out = sol.mergeNodes(head)
        output = []
        while out:
            output.append(out.val)
            out = out.next
        print(output)
        self.assertEqual(output, exp)
         
        exp = [1,3,4]
        curr = head = ListNode(0)
        for i in [1,0,3,0,2,2,0]:
            curr.next = ListNode(i)
            curr = curr.next
        out = sol.mergeNodes(head)
        output = []
        while out:
            output.append(out.val)
            out = out.next
        print(output)
        self.assertEqual(output, exp)


if __name__ == '__main__':
    unittest.main()
