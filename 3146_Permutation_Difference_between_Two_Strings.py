import unittest


class Solution:
    """3146. Permutation Difference between Two Strings."""
    
    def findPermutationDifference(self, s: str, t: str) -> int:
        ss, tt = list(s), list(t)
        return sum([abs(i - tt.index(ss[i])) for i in range(len(ss))])


class TestSolution(unittest.TestCase):    

    def test_findPermutationDifferenceI(self):
        sol = Solution()
        
        self.assertEqual(sol.findPermutationDifference(s = "abc", t = "bac"), 2)
        self.assertEqual(sol.findPermutationDifference(s = "abcde", t ="edbac"), 12)


if __name__ == "__main__":
    unittest.main()
