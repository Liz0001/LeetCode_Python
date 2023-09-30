import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: ['TreeNode'], val: int) -> ['TreeNode']:
        if root is None:
            return None
        elif val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return root
            

class TestSolution(unittest.TestCase):
    """700. Search in a Binary Search Tree."""

    def test_searchBST(self):
        sol = Solution()
        
        n1 = TreeNode(4)
        n2 = TreeNode(2)
        n3 = TreeNode(7)
        n4 = TreeNode(1)
        n5 = TreeNode(3)
        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5  
        val = 2
        exp = n2
        out = sol.searchBST(n1, val)
        self.assertEqual(out, exp)
        
        
        n1 = TreeNode(4)
        n2 = TreeNode(2)
        n3 = TreeNode(7)
        n4 = TreeNode(1)
        n5 = TreeNode(3)
        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        val = 5
        exp = None
        out = sol.searchBST(n1, val)
        self.assertEqual(out, exp) 


if __name__ == '__main__':
    unittest.main()
