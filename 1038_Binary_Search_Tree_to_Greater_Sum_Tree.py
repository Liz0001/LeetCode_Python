import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.s = 0
        
        def bfs(node):
            if node is None:
                return
            
            bfs(node.right)
            self.s += node.val
            node.val = self.s
            bfs(node.left)
            
        bfs(root)
        return root


def bfs_test(node, arr):
    if node is None:
        return
    
    bfs_test(node.left, arr)
    arr.append(node.val) 
    bfs_test(node.right, arr)
    
    return arr


class TestSolution(unittest.TestCase):
    """1038. Binary Search Tree to Greater Sum Tree."""

    def test_bstToGst(self):
        sol = Solution()

        root = TreeNode(4)
        n2 = TreeNode(1)
        n3 = TreeNode(6)
        n4 = TreeNode(0)
        n5 = TreeNode(2)
        n6 = TreeNode(5)
        n7 = TreeNode(7)
        n8 = TreeNode(3)
        n9 = TreeNode(8)
        root.left = n2
        root.right = n3
        n2.left = n4
        n2.right = n5
        n5.right = n8
        n3.left = n6
        n3.right = n7
        n7.right = n9
        exp = sorted([30,36,21,36,35,26,15,33,8])[::-1]
        out = sol.bstToGst(root)
        res = bfs_test(out, [])
        self.assertEqual(res, exp)

        root = TreeNode(0)
        n2 = TreeNode(1)
        root.right = n2
        exp = [1,1]
        out = sol.bstToGst(root)
        res = bfs_test(out, [])
        self.assertEqual(res, exp)
        

if __name__ == '__main__':
    unittest.main()
