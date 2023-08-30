import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    length = 0
    path = []
    depth = 0
    d = 0
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.dfs(root)
        print(self.depth)
        return 0
    
    
    
    def dfs(self, node):
        
        self.d += 1
        if node.left:
            self.dfs(node.left)
            # self.depth = max(self.d, self.depth)
            
        if node.right:
            self.dfs(node.right)
            # self.depth = max(self.d, self.depth)
        
        
        self.d -= 1
        self.depth = max(self.d, self.depth)
        # print(node.val)
        

class TestSolution(unittest.TestCase):
    """1372. Longest ZigZag Path in a Binary Tree."""

    def test_longestZigZag(self):
        sol = Solution()
        
        root = TreeNode(1)
        n2 = TreeNode(1)
        n3 = TreeNode(1)
        n4 = TreeNode(1)
        n5 = TreeNode(1)
        n6 = TreeNode(1)
        n7 = TreeNode(1)
        n8 = TreeNode(1)
        root.right = n2
        n2.left = n3
        n2.right = n4
        n4.left = n5
        n4.right = n6
        n5.right = n7
        n7.right = n8
        exp = 3
        out  = sol.longestZigZag(root)
        # self.assertEqual(out, exp)
        
        root = TreeNode(1)
        n2 = TreeNode(1)
        n3 = TreeNode(1)
        n4 = TreeNode(1)
        n5 = TreeNode(1)
        n6 = TreeNode(1)
        n7 = TreeNode(1)
        root.left = n2
        root.right = n3
        n2.right = n4
        n4.left = n5
        n4.right = n6
        n5.right = n7
        exp = 4
        # out  = sol.longestZigZag(root)
        # self.assertEqual(out, exp)

        root = TreeNode(1)
        exp = 0
        # out  = sol.longestZigZag(root)
        # self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
