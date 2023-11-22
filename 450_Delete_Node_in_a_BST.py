import unittest


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: ['TreeNode'], key: int) -> ['TreeNode']:
        if root is None:
            return None
    
        if root.val == key:
            print("Found, now lets remove:", key)

            if root.right is None and root.left is None:
                root = None
                return None
                
            elif root.right is None:
                return root.left
                
            elif root.left is None:
                return root.right
            
            else:
                pass
            
       
        
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
 
            
        
        return root
    
    
 

    def test_bst(self, root, key):
        if root is None:
            return None
        
        print("Node ", root.val)
        if root.val == key:
            print("Testing failed:", key, 'found')
        
        elif root.val < key:
            self.test_bst(root.right, key)
        elif root.val > key:
            self.test_bst(root.left, key)
        

class TestSolution(unittest.TestCase):
    """450. Delete Node in a BST."""

    def test_(self):
        sol = Solution()

        # Input: root = [5,3,6,2,4,null,7], key = 3
        # Output: [5,4,6,2,null,null,7]    
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
        # key = 3
        key = 6
        exp = n1
        out = sol.deleteNode(n1, key)
        print("")
        sol.test_bst(n1, key)
        # self.assertEqual(exp, out)

        # Input: root = [5,3,6,2,4,null,7], key = 0
        # Output: [5,3,6,2,4,null,7]
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
        # out = sol.deleteNode(n1, key)
        # self.assertEqual(exp, out)
        
        # root = [], key = 0
        # Output: None
        n1 = None
        key = 0
        exp = None
        # out = sol.deleteNode(n1, key)
        # self.assertEqual(exp, out)

if __name__== '__main__':
    unittest.main()
