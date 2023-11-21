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
        
        print(root.val)
        prev = root
        if root.val == key:
            print("Found, now lets remove:", key)
            self.delNode(root, key, prev)
        
        elif root.val < key:
            self.deleteNode(root.right, key)
        elif root.val > key:
            self.deleteNode(root.left, key)
        
        return root


    def delNode(self, curr, val, prev):
        # case 0 - root
        # if prev == None:
            
        
        # case 1 - no child - leaf
        if curr.right is None and curr.left is None:
            if prev.right is not None and prev.right == val:
                prev.right = None
            elif prev.left == val:
                prev.left == None
            
        # case 2 - 1 child - ??
        # elif curr.right is None or curr.left is None:
        #     if prev.right is not None and prev.right == val:
        #         if curr.right is not None:
        #             prev.right = curr.right
        #         elif curr.left is not None:
        #             prev.right = curr.left
        #     elif prev.left is not None and prev.left == val:
        #         if curr.right is not None:
        #             prev.right = curr.right
        #         elif curr.left is not None:
        #             prev.right = curr.left
        #         prev.left == None
        
        
        # case 3 - 2 children - ??
        # if node.right and :
        #     pass

    def test_bst(self, root, key):
        if root is None:
            return None
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
        key = 3
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
