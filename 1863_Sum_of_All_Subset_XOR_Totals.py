import unittest
from typing import List
from itertools import combinations


class TestSolution(unittest.TestCase):
    
    def test_subsetXORSum(self):
        sol = Solution()
        
        self.assertEqual(sol.subsetXORSum(nums = [1,3]), 6)
        self.assertEqual(sol.subsetXORSum(nums = [5,1,6]), 28)
        self.assertEqual(sol.subsetXORSum(nums = [3,4,5,6,7,8]), 480)


class Solution:
    """1863. Sum of All Subset XOR Totals."""
    
    def subsetXORSum(self, nums: List[int]) -> int:
        xor = [0] + nums
        
        for i in range(2, len(nums)+1):
            x = list(combinations(nums, i))
            for j in x:
                c = j[0]
                for k in range(1, len(j)):
                    c = c ^ j[k]
                xor.append(c)
        return sum(xor)


if __name__ == "__main__":
    unittest.main()
