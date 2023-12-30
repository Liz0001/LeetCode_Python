import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def constructMaximumBinaryTree(self, nums: [int]) -> [TreeNode]:
        if len(nums) == 0:
            return    
        elif len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 2:
            max_ind = nums.index(max(nums))
            node = TreeNode(nums[max_ind])
            if max_ind == 1:
                node.left = self.constructMaximumBinaryTree([nums[0]])
            else:
                node.right = self.constructMaximumBinaryTree([nums[1]])
            return node       
            
        else:
            max_ind = nums.index(max(nums))
            node = TreeNode(nums[max_ind])
            left = nums[:max_ind] 
            right = nums[max_ind+1:] 
            node.left = self.constructMaximumBinaryTree(left)
            node.right = self.constructMaximumBinaryTree(right)
            
        return node
        
# 96.66%

def tree_to_list(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result
            
        
class TestSolution(unittest.TestCase):
    """654. Maximum Binary Tree."""

    def test_constructMaximumBinaryTree(self):
        sol = Solution()

        nums = [3,2,1,6,0,5]
        exp = [6,3,5,None,2,0,None,None,1]
        out = sol.constructMaximumBinaryTree(nums)
        out_list = tree_to_list(out)
        self.assertEqual(out_list, exp)
        
        nums = [3,2,1]
        exp = [3,None,2,None,1]
        out = sol.constructMaximumBinaryTree(nums)
        out_list = tree_to_list(out)
        self.assertEqual(out_list, exp)


if __name__ == '__main__':
    unittest.main()
