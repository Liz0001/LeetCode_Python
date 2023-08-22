import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    count = 0
    
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        self.dfs(root, root.val)
        s = self.count
        self.count = 0
        return s
    
    def dfs(self, node, prev=None):
        
        if prev is None:
            prev = node.val
            self.count += 1
            
        elif node.val >= prev:
            self.count += 1
            prev = node.val
                
        if node.left:
            self.dfs(node.left, prev)
             
        if node.right:
            self.dfs(node.right, prev)
        

class TestSolution(unittest.TestCase):
    """1448. Count Good Nodes in Binary Tree."""
    
    def test_goodNodes(self):
        sol = Solution()
        
        # root = [3,1,4,3,null,1,5]
        n1 = TreeNode(3)
        n2 = TreeNode(1)
        n3 = TreeNode(4)
        n4 = TreeNode(3)
        n5 = TreeNode(1)
        n6 = TreeNode(5)
        n1.left = n2
        n1.right = n3
        n2.left = n4
        n3.left = n5
        n3.right = n6
        exp = 4
        out = sol.goodNodes(n1)
        self.assertEqual(out, exp)

        # root = [3,3,null,4,2]
        n1 = TreeNode(3)
        n2 = TreeNode(3)
        n3 = TreeNode(4)
        n4 = TreeNode(2)
        n1.left = n2
        n2.left = n3
        n2.right = n4
        exp = 3
        out = sol.goodNodes(n1)
        self.assertEqual(out, exp)
        
        # root = [1]
        n1 = TreeNode(1)
        exp = 1
        out = sol.goodNodes(n1)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
