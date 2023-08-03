import unittest
from collections import Counter

class Solution:
    def closeStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b) or set(a) != set(b):
            return False
        if a == b:
            return True

        aa = list(Counter(a).values())
        bb = list(Counter(b).values())
        aa.sort()
        bb.sort()
        if aa == bb:
            return True

        return False


class TestSolution(unittest.TestCase):
    """1657. Determine if Two Strings Are Close."""
    def test_closeStrings1(self):
        sol = Solution()
        word1 = "abc"
        word2 = "bca"
        ans = sol.closeStrings(word1, word2)
        self.assertTrue(ans)

    def test_closeStrings2(self):
        sol = Solution()
        word1 = "a"
        word2 = "aa"
        ans = sol.closeStrings(word1, word2)
        self.assertFalse(ans)

    def test_closeStrings3(self):
        sol = Solution()
        word1 = "cabbba"
        word2 = "abbccc"
        ans = sol.closeStrings(word1, word2)
        self.assertTrue(ans)

    def test_closeStrings4(self):
        sol = Solution()
        word1 = "aaabbbbccddeeeeefffff"
        word2 = "aaaaabbcccdddeeeeffff"
        ans = sol.closeStrings(word1, word2)
        self.assertFalse(ans)

    def test_closeStrings5(self):
        sol = Solution()
        word1 = "abbzccca"
        word2 = "babzzczc"
        ans = sol.closeStrings(word1, word2)
        self.assertTrue(ans)

    def test_closeStrings6(self):
        sol = Solution()
        word1="uau"
        word2="ssx"
        ans = sol.closeStrings(word1, word2)
        self.assertFalse(ans)


if __name__ == '__main__':
    unittest.main()
