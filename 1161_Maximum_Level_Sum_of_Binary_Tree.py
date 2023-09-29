import unittest
import operator


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: ['TreeNode']) -> int:
        self.tree_levels = self.map_the_tree_level(root)
        self.level_sum = {}
        self.dfs(root, [])
        print(self.level_sum)
        return max(self.level_sum.items(), key=operator.itemgetter(1))[0]
       
        
    def dfs(self, root, path):
        if root is None:
            return
        
        level = self.tree_levels[root]
        if self.level_sum.get(level):
            self.level_sum[level] = self.level_sum.get(level) + root.val
        else:
            self.level_sum[level] = root.val
        
        self.dfs(root.left, path)
        self.dfs(root.right, path)
        
    
    def map_the_tree_level(self, root):
        tree_levels = {}
        level = 1
        queue = [root, None]

        while len(queue) > 1:
            p = queue.pop(0)
            if p == None:
                level += 1
                queue.append(None)
                if queue[0] == None:
                    break
                else:
                    continue
                
            tree_levels[p] = level
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
            
        return tree_levels


class TestSolution(unittest.TestCase):
    """1161. Maximum Level Sum of a Binary Tree."""
    
    def test_maxLevelSum(self):
        sol = Solution()

        # Input: root = [1,7,0,7,-8,null,null]
        # Output: 2
        n1 = TreeNode(1)
        n2 = TreeNode(7)
        n3 = TreeNode(0)
        n4 = TreeNode(7)
        n5 = TreeNode(-8)
        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        exp = 2
        out = sol.maxLevelSum(n1)
        self.assertEqual(out, exp)

        # Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
        # Output: 2
        n1 = TreeNode(989)
        n2 = TreeNode(10250)
        n3 = TreeNode(98693)
        n4 = TreeNode(-89388)
        n5 = TreeNode(-32127)
        n1.right = n2
        n2.left = n3
        n2.right = n4
        n4.right = n5
        exp = 2
        out = sol.maxLevelSum(n1)
        # self.assertEqual(out, exp)
        

if __name__ == '__main__':
    unittest.main()
