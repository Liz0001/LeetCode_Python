import unittest
from typing import List


class Solution:
    """1684. Count the Number of Consistent Strings."""
    
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return [sum([-1 for j in i if j not in allowed]) for i in words].count(0)


class TestSolution(unittest.TestCase):

    def test_countConsistentStrings(self):
        sol = Solution()
        
        self.assertEqual(sol.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]), 2)
        self.assertEqual(sol.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]), 7)
        self.assertEqual(sol.countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]), 4)


if __name__ == "__main__":
    unittest.main()
