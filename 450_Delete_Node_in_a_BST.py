import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: ['TreeNode'], key: int) -> ['TreeNode']:
        if root is None:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            
        elif root.val > key:
            root.left = self.deleteNode(root.left, key) 
        
        else:
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                m = self.find_min(root.right)
                root.val = m
                root.right = self.deleteNode(root.right, m)
                return root
            
        return root


    def find_min(self, root):
        while root.left is not None:
            root = root.left
        return root.val
        

class TestSolution(unittest.TestCase):
    """450. Delete Node in a BST."""

    def test_deleteNode(self):
        sol = Solution()

        n1 = TreeNode(5)
        n2 = TreeNode(3)
        n3 = TreeNode(6)
        n4 = TreeNode(2)
        n5 = TreeNode(4)
        n6 = TreeNode(7)
        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        n3.right = n6
        key = 3
        exp = n1
        out = sol.deleteNode(n1, key)
        self.assertEqual(exp, out)

        n1 = TreeNode(5)
        n2 = TreeNode(3)
        n3 = TreeNode(6)
        n4 = TreeNode(2)
        n5 = TreeNode(4)
        n6 = TreeNode(7)
        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        n3.right = n6
        key = 0
        exp = n1
        out = sol.deleteNode(n1, key)
        self.assertEqual(exp, out)
        
        n1 = None
        key = 0
        exp = None
        out = sol.deleteNode(n1, key)
        self.assertEqual(exp, out)


if __name__== '__main__':
    unittest.main()
