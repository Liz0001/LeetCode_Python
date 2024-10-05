import unittest
from typing import List
from collections import Counter


class Solution:
    """3289. The Two Sneaky Numbers of Digitville."""
    
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = Counter(nums).most_common(2)
        n.sort()
        return [n[0][0], n[1][0]]


class TestSolution(unittest.TestCase):

    def test_getSneakyNumbers(self):
        sol = Solution()
        
        self.assertEqual(sol.getSneakyNumbers([0,1,1,0]), [0,1])
        self.assertEqual(sol.getSneakyNumbers([0,3,2,1,3,2]), [2,3])
        self.assertEqual(sol.getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2]), [4,5])


if __name__ == "__main__":
    unittest.main()
