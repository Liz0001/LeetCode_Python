from typing import List
import unittest
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # slower one
        # my_set = set(arr)        
        # return len(set([arr.count(x) for x in my_set])) == len(my_set)

        # faster solution
        occ = Counter(arr)
        return len(occ) == len(set(occ.values()))


class TestSolution(unittest.TestCase):
    """1207. Unique Number of Occurrences."""

    def test_uniqueOccurrences1(self):
        sol = Solution()
        arr = [1,2,2,1,1,3]
        ans = sol.uniqueOccurrences(arr)
        self.assertTrue(ans)

    def test_uniqueOccurrences2(self):
        sol = Solution()
        arr = [1,2]
        ans = sol.uniqueOccurrences(arr)
        self.assertFalse(ans)

    def test_uniqueOccurrences3(self):
        sol = Solution()
        arr = [-3,0,1,-3,1,1,1,-3,10,0]
        ans = sol.uniqueOccurrences(arr)
        self.assertTrue(ans)


if __name__ == '__main__':
    unittest.main()
