import unittest
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    
class Solution:
    def rightSideView(self, root: 'TreeNode') -> List[int]:
        if root is None:
            return None
        self.level_map = {}
        self.sideView = [root.val]
        self.level = 0
        
        self.mapping_tree_level(root)
        self.dfs(root)
        # print(self.sideView)
        return self.sideView


    def dfs(self, node):
        if node is None:
            return
        
        if self.level_map[node] > self.level:
            self.level += 1
            self.sideView.append(node.val)
        
        self.dfs(node.right)
        self.dfs(node.left)
            
    
    def mapping_tree_level(self, root):
        level = 0
        queue = [root, None]
        
        while len(queue) > 0:
            popped = queue.pop(0)
            
            if popped == None:
                level += 1
                queue.append(None)
                if queue[0] == None:
                    break
                else:
                    continue
            
            self.level_map[popped] = level
            if popped.left:
                queue.append(popped.left)
            
            if popped.right:
                queue.append(popped.right)


class TestSolution(unittest.TestCase):
    """199. Binary Tree Right Side View."""

    def test_rightSideView(self):
        sol = Solution()

        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n5 = TreeNode(5)
        n4 = TreeNode(4)
        n1.left = n2
        n1.right = n3
        n2.right = n5
        n3.right = n4
        exp = [1,3,4]
        out = sol.rightSideView(n1)
        self.assertEqual(out, exp)
        
        n1 = TreeNode(1)
        n2 = TreeNode(3)
        n1.right = n2
        exp = [1,3]
        out = sol.rightSideView(n1)
        self.assertEqual(out, exp)
        
        exp = None
        out = sol.rightSideView(None)
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
        exp = [3,1,8,4]
        out = sol.rightSideView(n1)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
