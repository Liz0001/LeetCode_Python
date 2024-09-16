import unittest

class Solution:
    """3110. Score of a String."""
    
    def scoreOfString(self, s: str) -> int:
        val = 0
        ss = list(s)
        for i in range(len(ss)-1):
            val += abs(ord(ss[i])-ord(ss[i+1]))

        return val


class TestSolution(unittest.TestCase):
    """Testing."""

    def test_scoreOfString(self):
        sol = Solution()
        self.assertEqual(sol.scoreOfString("hello"), 13)
        self.assertEqual(sol.scoreOfString("zaz"), 50)


if __name__ == "__main__":
    unittest.main()
