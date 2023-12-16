import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.d = {}
        self.dfs(root, [])
        c = 0
        for i in self.d:
            x = self.d.get(i)
            if i.val == int(sum(x)//len(x)):
                c += 1
        return c
    

    def dfs(self, node, arr):
        if node is None:
            return
        
        arr.append(node)
        self.d[node] = []
        
        self.dfs(node.left, arr)
        self.dfs(node.right, arr)
        
        for a in arr:
            self.d[a].append(node.val)
        arr.pop()


class TestSolution(unittest.TestCase):
    """2265. Count Nodes Equal to Average of Subtree."""

    def test_averageOfSubtree(self):
        sol = Solution()

        head = TreeNode(4)
        n2 = TreeNode(8)
        n3 = TreeNode(5)
        n4 = TreeNode(0)
        n5 = TreeNode(1)
        n6 = TreeNode(6)
        head.left = n2
        head.right = n3
        n2.left = n4
        n2.right = n5
        n3.right = n6
        exp = 5
        out = sol.averageOfSubtree(head)
        self.assertEqual(out, exp)
         
        head = TreeNode(1)
        exp = 1
        out = sol.averageOfSubtree(head)
        self.assertEqual(out, exp)
        
        head = TreeNode(0)
        n2 = TreeNode(0)
        n3 = TreeNode(0)
        head.left = n2
        head.right = n3
        exp = 3
        out = sol.averageOfSubtree(head)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
