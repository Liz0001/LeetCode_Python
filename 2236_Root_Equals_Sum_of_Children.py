"""
2236. Root Equals Sum of Children from Leetcode.

You are given the root of a binary tree that consists
of exactly 3 nodes: the root, its left child, and its right child.

Return true if the value of the root is equal to the
sum of the values of its two children, or false otherwise.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    """TreeNode."""

    def __init__(self, val=0, left=None, right=None):
        """Init."""
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Root Equals Sum of Children Class."""

    def checkTree(self, root: Optional[TreeNode]) -> bool:
        """Root Equals Sum of Children Function."""
        return root.val == (root.right.val + root.left.val)
