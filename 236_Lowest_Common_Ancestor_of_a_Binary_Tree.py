import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.d = {}
        self.node = {}
        self.d[root.val] = []
        self.dfs(root, root.val, [])
        minn = 0
        s = len(self.d[root.val])
        for i in self.d:
            if p.val in self.d[i] and q.val in self.d[i]:
                minn = i
                if s > len(self.d[i]):
                    s = i        
        return self.node[minn]


    def dfs(self, node, val, path):
        if node is None:
            return
        
        path.append(node.val)
        self.d[node.val] = []
        self.node[node.val] = node
        [self.d[i].append(node.val) for i in path]
        
        self.dfs(node.left, node.val, path)
        self.dfs(node.right, node.val, path)
        
        path.pop()
        
        

class TestSolution(unittest.TestCase):
    """236. Lowest Common Ancestor of a Binary Tree."""

    def test_lowestCommonAncestor(self):
        sol = Solution()
        
        n1 = TreeNode(3)
        n2 = TreeNode(5)
        n3 = TreeNode(1)
        n4 = TreeNode(6)
        n5 = TreeNode(2)
        n6 = TreeNode(0)
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
        exp = n1
        out = sol.lowestCommonAncestor(n1, n2, n3)
        self.assertEqual(out, exp)

        n1 = TreeNode(3)
        n2 = TreeNode(5)
        n3 = TreeNode(1)
        n4 = TreeNode(6)
        n5 = TreeNode(2)
        n6 = TreeNode(0)
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
        exp = n2
        out = sol.lowestCommonAncestor(n1, n2, n9)
        self.assertEqual(out, exp)
        
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n1.left = n2
        exp = n1
        out = sol.lowestCommonAncestor(n1, n1, n2)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
