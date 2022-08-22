"""
1290. Convert Binary Number in a Linked List to Integer from Leetcode.

Given head which is a reference node to a singly-linked list.
The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.
"""


# Definition for singly-linked list.
class ListNode:
    """ListNode."""

    def __init__(self, val=0, next=None):
        """Init."""
        self.val = val
        self.next = next

    def __str__(self) -> str:
        """Print value."""
        return str(self.val)


class Solution:
    """Convert Binary Number in a Linked List to Integer Class."""

    def getDecimalValue(self, head: ListNode) -> int:
        """Convert Binary Number in a Linked List to Integer."""
        stack = []

        def getVal(head: ListNode, stack):
            stack.append(head.val)
            if head.next is not None:

                return getVal(head.next, stack)
        stack.append(getVal(head, stack))
        power = 1
        res = 0
        for i in range(len(stack)-1, -1, -1):
            if stack[i] is not None:
                res = res + (stack[i] * power)
                power = power + power
        return res


def main():
    """Solution."""
    node1 = ListNode(1)
    node2 = ListNode(0)
    node3 = ListNode(1)
    node4 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    head = node1
    s = Solution()
    # head = [1, 0, 1]      # output: 5
    answer = s.getDecimalValue(head)
    print(answer)


if __name__ == "__main__":
    main()
