import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node, ts):
            if node is None:
                return 0
            
            res = 0
            if node.val == ts:
                res += 1
                
            res += dfs(node.left, ts-node.val)
            res += dfs(node.right, ts-node.val)
            return res
        
        if root is None:
            return 0
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)


class SolutionTest(unittest.TestCase):
    """437. Path Sum III."""

    def test_pathSum(self):
        sol = Solution()
        
        root = TreeNode(10)
        n2 = TreeNode(5)        
        n3 = TreeNode(-3)        
        n4 = TreeNode(3)        
        n5 = TreeNode(2)        
        n6 = TreeNode(11)        
        n7 = TreeNode(3)        
        n8 = TreeNode(-2)        
        n9 = TreeNode(1)        
        root.left = n2
        root.right = n3
        n2.left = n4
        n2.right = n5
        n3.right = n6
        n5.right = n9
        n4.left = n7
        n4.right = n8
        targetSum = 8
        exp = 3
        out = sol.pathSum(root, targetSum)
        self.assertEqual(exp, out)
        
        root = TreeNode(1)
        n2 = TreeNode(-2)        
        n3 = TreeNode(-3)        
        n4 = TreeNode(1)        
        n5 = TreeNode(3)        
        n6 = TreeNode(-2)        
        n7 = TreeNode(-1)        
        root.left = n2
        root.right = n3
        n2.left = n4
        n2.right = n5
        n4.left = n7
        n3.left = n6
        targetSum = 3
        exp = 1
        out = sol.pathSum(root, targetSum)
        self.assertEqual(exp, out)

        root = TreeNode(0)
        n2 = TreeNode(1)        
        n3 = TreeNode(1)        
        root.left = n2
        root.right = n3
        targetSum = 1
        exp = 4
        out = sol.pathSum(root, targetSum)
        self.assertEqual(exp, out)
        
        root = TreeNode(0)
        n2 = TreeNode(1)        
        n3 = TreeNode(1)        
        root.left = n2
        root.right = n3
        targetSum = 0
        exp = 1
        out = sol.pathSum(root, targetSum)
        self.assertEqual(exp, out)
        
        root = TreeNode(-2)
        n2 = TreeNode(-3)        
        root.right = n2
        targetSum = -3
        exp = 1
        out = sol.pathSum(root, targetSum)
        self.assertEqual(exp, out)
        
        root = TreeNode(1)
        n2 = TreeNode(0)        
        n3 = TreeNode(1)        
        n4 = TreeNode(1)        
        n5 = TreeNode(2)        
        n6 = TreeNode(0)        
        n7 = TreeNode(-1)        
        n8 = TreeNode(0)        
        n9 = TreeNode(1)        
        n10 = TreeNode(-1)        
        n11 = TreeNode(0)        
        n12 = TreeNode(-1)        
        n13 = TreeNode(0)        
        n14 = TreeNode(1)        
        n15 = TreeNode(0)        
        root.left = n2
        root.right = n3
        n2.left = n4
        n2.right = n5
        n3.left = n6
        n3.right = n7
        n4.left = n8
        n4.right = n9
        n5.left = n10
        n5.right = n11
        n6.left = n12
        n6.right = n13
        n7.left = n14
        n7.right = n15
        targetSum = 2
        exp = 13
        out = sol.pathSum(root, targetSum)
        self.assertEqual(exp, out)


if __name__ == '__main__':
    unittest.main()
