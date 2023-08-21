import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.dfs(root1, []) == self.dfs(root2, [])
    
    def dfs(self, node, leaves):
        
        if node is None:
            return
        
        if node.left:
            self.dfs(node.left, leaves)
            
        if node.right:
            self.dfs(node.right, leaves)
        
        if node.right == None and node.left == None:
            leaves.append(node.val)

        return leaves


class TestSolution(unittest.TestCase):
    """872. Leaf-Similar Trees."""

    def test_leafSimilar(self):
        sol = Solution()
        
        # root1 = [3,5,1,6,2,9,8,null,null,7,4]
        # root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
        n1 = TreeNode(3)
        n2 = TreeNode(5)
        n3 = TreeNode(1)
        n4 = TreeNode(6)
        n5 = TreeNode(2)
        n6 = TreeNode(9)
        n7 = TreeNode(8)
        n8 = TreeNode(7)
        n9 = TreeNode(4)
        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        n5.left = n8
        n5.right = n9
        n3.left = n6
        n3.right = n7
        
        tn1 = TreeNode(3)
        tn2 = TreeNode(5)
        tn3 = TreeNode(1)
        tn4 = TreeNode(6)
        tn5 = TreeNode(7)
        tn6 = TreeNode(4)
        tn7 = TreeNode(2)
        tn8 = TreeNode(9)
        tn9 = TreeNode(8)
        tn1.left = tn2
        tn1.right = tn3
        tn2.left = tn4
        tn2.right = tn5
        tn3.left = tn6
        tn3.right = tn7
        tn7.left = tn8
        tn7.right = tn9
        
        exp = True
        out = sol.leafSimilar(n1, tn1)
        self.assertEqual(out, exp)
        
        
        # root1 = [1,2,3]
        # root2 = [1,3,2]
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n1.left = n2
        n1.right = n3
        
        tn1 = TreeNode(1)
        tn2 = TreeNode(3)
        tn3 = TreeNode(2)
        tn1.left = tn2
        tn1.right = tn3
        
        exp = False
        out = sol.leafSimilar(n1, tn1)
        self.assertEqual(out, exp)
        
        # root1 = [1]
        # root2 = [1]
        n1 = TreeNode(1)
        tn1 = TreeNode(1)
        
        exp = True
        out = sol.leafSimilar(n1, tn1)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
