import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.summ = 0
        self.child_to_add = []
        self.dfs(root, root)
        return self.summ
  
   
    def dfs(self, node, parent):
        if node is None:
            return
            
        if parent in self.child_to_add:
            self.summ += node.val
            
        parent = node  
        
        if node.val % 2 == 0:
            if node.left is not None:
                self.child_to_add.append(node.left)
            if node.right is not None:
                self.child_to_add.append(node.right)
            
        self.dfs(node.left, parent)
        self.dfs(node.right, parent)
        
        
class TestSolution(unittest.TestCase):
    """1315. Sum of Nodes with Even-Valued Grandparent."""

    def test_sumEvenGrandparent(self):
        sol = Solution()

        root = TreeNode(6)
        n2 = TreeNode(7)
        n3 = TreeNode(8)
        n4 = TreeNode(2)
        n5 = TreeNode(7)
        n6 = TreeNode(1)
        n7 = TreeNode(3)
        n8 = TreeNode(9)
        n9 = TreeNode(1)
        n10 = TreeNode(4)
        n11 = TreeNode(5)
        root.left = n2
        root.right = n3
        n2.left = n4
        n2.right = n5
        n4.left = n8
        n5.left = n9
        n5.right = n10
        n3.left = n6
        n3.right = n7
        n7.right = n11
        exp = 18
        out = sol.sumEvenGrandparent(root)
        self.assertEqual(exp, out)
        
        root = TreeNode(1)
        exp = 0
        out = sol.sumEvenGrandparent(root)
        self.assertEqual(exp, out)
        
        root = TreeNode(6)
        n2 = TreeNode(8)
        n3 = TreeNode(7)
        n4 = TreeNode(2)
        n5 = TreeNode(7)
        n6 = TreeNode(1)
        n7 = TreeNode(3)
        n8 = TreeNode(9)
        n9 = TreeNode(1)
        n10 = TreeNode(4)
        n11 = TreeNode(5)
        root.left = n2
        root.right = n3
        n2.left = n4
        n2.right = n5
        n4.left = n8
        n5.left = n9
        n5.right = n10
        n3.left = n6
        n3.right = n7
        n7.right = n11
        exp = 27
        out = sol.sumEvenGrandparent(root)
        self.assertEqual(exp, out)


if __name__ == '__main__':
    unittest.main()
