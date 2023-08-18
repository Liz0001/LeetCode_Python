
""" BEST SOLUTION. """

import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
    
    def dfs(self, root):
        if root is None:
            return 0
        return 1 + max(self.dfs(root.left), self.dfs(root.right))


class TestSolution(unittest.TestCase):
    """104. Maximum Depth of Binary Tree."""

    def test_maxDepth(self):
        sol = Solution()
        
        # [3,9,20,null,null,15,7]
        n1 = TreeNode(3)
        n2 = TreeNode(9)
        n3 = TreeNode(20)
        n4 = TreeNode(15)
        n5 = TreeNode(7)
        n1.left = n2
        n1.right = n3
        n3.left = n4
        n3.right = n5
        exp = 3
        out = sol.maxDepth(n1)
        self.assertEqual(out, exp)
        
        # [1,null,2]
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n1.right = n2
        exp = 2
        out = sol.maxDepth(n1)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
