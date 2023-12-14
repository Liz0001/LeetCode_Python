import unittest


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        binary = bin(n).split('b')[1]
        if binary[:2] != (binary[:-2])[::-1]:
            return False
        return True


class TestSolution(unittest.TestCase):
    """2396. Strictly Palindromic Number."""

    def test_isStrictlyPalindromic(self):
        sol = Solution()
        
        n = 9
        exp = False
        out = sol.isStrictlyPalindromic(n)
        self.assertEqual(exp, out)
        
        n = 4
        exp = False
        out = sol.isStrictlyPalindromic(n)
        self.assertEqual(exp, out)


if __name__ == "__main__":
    unittest.main()
