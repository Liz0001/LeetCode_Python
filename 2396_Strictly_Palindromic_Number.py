import unittest


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        binary = bin(n)
        b = binary.split('b')[1]
        bb = list(b)
        dd = bb[::-1]
        print()
        print(list(b))
        print()
        print(list(b)[:2],(list(b)[:-2])[::-1])
        for i in range(2, n-1):
            if list(b)[:2] != (list(b)[:-2])[::-1]:
                return False
        # print(list(b)[:2] == (list(b)[:-2])[::-1])
        
        
        
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
