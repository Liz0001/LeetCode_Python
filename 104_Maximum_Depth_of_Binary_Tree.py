import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    d = 0
    depth = 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.get_depths(root)
        ans = self.d
        self.d = 0
        self.depth = 1
        return ans
    
    def get_depths(self, root):
        if root.left:
            self.depth += 1
            self.get_depths(root.left)
            self.depth -= 1
           
        if root.right:
            self.depth += 1
            self.get_depths(root.right)
            self.depth -= 1
            
        if root.right is None and root.left is None:
            self.d = max(self.d, self.depth)
        
        return self.depth


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
