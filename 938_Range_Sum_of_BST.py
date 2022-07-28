"""
938. Range Sum of BST from Leetcode.

Given the root node of a binary search tree and
two integers low and high, return the sum of
values of all nodes with a value
in the inclusive range [low, high].
"""
from doctest import REPORT_ONLY_FIRST_FAILURE
from typing import Optional

from matplotlib.pyplot import stackplot


# Definition for a binary tree node.
class TreeNode:
    """TreeNode."""

    def __init__(self, val=0, left=None, right=None):
        """InIt."""
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Range Sum of BST Class."""

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """Range Sum of BST."""
        stack = []

        def bst(root: Optional[TreeNode], low: int, high: int, stack) -> int:
            """Range Sum of BST."""
            if root is None:
                return 0
            if root is not None:
                bst(root.left, low, high, stack)
                bst(root.right, low, high, stack)
            if root.val <= high and root.val >= low:
                # print("the root", end=' ')
                # print(root.val)
                stack.append(root.val)
            return stack

        return sum(bst(root, low, high, stack))


def main():
    """Solution."""
    s = Solution()
    node1 = TreeNode(10)
    node2 = TreeNode(5)
    node3 = TreeNode(15)
    node4 = TreeNode(3)
    node5 = TreeNode(7)
    node6 = TreeNode(18)
    node1.right = node3
    node1.left = node2
    node2.right = node5
    node2.left = node4
    node3.right = node6
    # root = [10, 5, 15, 3, 7, None, 18]
    low = 7
    high = 15
    answer = s.rangeSumBST(node1, low, high)
    print(answer)


if __name__ == "__main__":
    main()
