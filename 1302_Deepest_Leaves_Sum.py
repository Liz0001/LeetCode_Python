import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: [TreeNode]) -> int:
        self.deepest_level = 0
        self.summ = 0
        self.bfs(root, 0)
        return self.summ
    
    
    def bfs(self, node, current_level):
        if node is None:
            return
        
        if current_level == self.deepest_level:
            self.summ += node.val
        if self.deepest_level < current_level:
            self.summ = node.val
            self.deepest_level = current_level
            
        current_level+=1
        self.bfs(node.left, current_level)
        self.bfs(node.right, current_level)


class TestSolution(unittest.TestCase):
    """1302. Deepest Leaves Sum."""

    def test_deepestLeavesSum(self):
        sol = Solution()
        
        head = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n5 = TreeNode(5)
        n6 = TreeNode(6)
        n7 = TreeNode(7)
        n8 = TreeNode(8)
        head.left = n2
        head.right = n3
        n2.left = n4
        n2.right = n5
        n4.left = n7
        n3.right = n6
        n6.right = n8
        exp = 15
        out = sol.deepestLeavesSum(head)
        self.assertEqual(exp, out)
        
        head = TreeNode(6)
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
        head.left = n2
        head.right = n3
        n2.left = n4
        n2.right = n5
        n4.left = n8
        n5.left = n9
        n5.right = n10
        n3.left = n6
        n3.right = n7
        n7.right = n11
        exp = 19
        out = sol.deepestLeavesSum(head)
        self.assertEqual(exp, out)


if __name__ == '__main__':
    unittest.main()
