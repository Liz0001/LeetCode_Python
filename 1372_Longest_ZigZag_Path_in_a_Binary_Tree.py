import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        self.depth = 0
        
        while stack:
            top = stack.pop()
            if top:
                stack.insert(0, top.left)
                stack.insert(0, top.right)
            
            self.dfs(top, 'L', -1)
            self.dfs(top, 'R', -1)
            
        # print("Depth:", self.depth)
        return self.depth
    
    
    def dfs(self, node, direction, count):
        if node is None:
            return
        
        count += 1
        self.depth = max(count, self.depth)
        
        if direction == 'R':
            self.dfs(node.left, 'L', count)
            
        if direction == 'L':
            self.dfs(node.right, 'R', count)

        

class TestSolution(unittest.TestCase):
    """1372. Longest ZigZag Path in a Binary Tree."""

    def test_longestZigZag(self):
        sol = Solution()
        
        root = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n5 = TreeNode(5)
        n6 = TreeNode(6)
        n7 = TreeNode(7)
        n8 = TreeNode(8)
        root.right = n2
        n2.left = n3
        n2.right = n4
        n4.left = n5
        n4.right = n6
        n5.right = n7
        n7.right = n8
        exp = 3
        out  = sol.longestZigZag(root)
        self.assertEqual(out, exp)
        
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
        self.assertEqual(out, exp)
        
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
        out  = sol.longestZigZag(root)
        self.assertEqual(out, exp)

        root = TreeNode(1)
        exp = 0
        out  = sol.longestZigZag(root)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
