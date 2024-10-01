import unittest
from typing import List


class Solution:
    """3190. Find Minimum Operations to Make All Elements Divisible by Three."""
    
    def minimumOperations(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            if (i+1) % 3 == 0:
                c += 1
            elif (i-1) % 3 == 0:
                c += 1
        return c


class TestSolution(unittest.TestCase):

    def test_minimumOperations(self):
        sol = Solution()
        
        self.assertEqual(sol.minimumOperations([1,2,3,4]), 3)
        self.assertEqual(sol.minimumOperations([3,6,9]), 0)


if __name__ == "__main__":
    unittest.main()
