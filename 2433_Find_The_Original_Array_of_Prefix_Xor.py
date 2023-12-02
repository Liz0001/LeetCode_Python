import unittest
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        for i in range(1, len(pref)):
            arr.append(pref[i-1]^pref[i])
        return arr


class TestSolution(unittest.TestCase):
    """2433. Find The Original Array of Prefix Xor."""

    def test_findArray(self):
        sol = Solution()
        
        pref = [5,2,0,3,1]
        exp =  [5,7,2,3,2]
        out = sol.findArray(pref)
        self.assertEqual(out, exp)
        
        pref = [13]
        exp =  [13]
        out = sol.findArray(pref)
        self.assertEqual(out, exp)


if __name__ == "__main__":
    unittest.main()
