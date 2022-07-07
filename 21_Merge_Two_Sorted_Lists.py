"""21. Merge Two Sorted Lists from Leetcode.

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         """."""
#         self.val = val
#         self.next = next


class Solution:
    """Merge Two Sorted Lists Class."""

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:    # noqa
        """Merge Two Sorted Lists Function."""
        if list1 is []:
            return list2
        if list2 is []:
            return list1

        headnode = ListNode()
        tailnode = headnode

        while list1 and list2:
            if list1.val <= list2.val:
                tailnode.next = list1
                list1 = list1.next
                tailnode = tailnode.next

            else:
                tailnode.next = list2
                list2 = list2.next
                tailnode = tailnode.next

        if list1:
            tailnode.next = list1
        if list2:
            tailnode.next = list2

        return headnode.next
