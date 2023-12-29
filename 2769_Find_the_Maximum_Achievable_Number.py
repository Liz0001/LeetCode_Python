import unittest


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t*2
         

class TestSolution(unittest.TestCase):
    """2769. Find the Maximum Achievable Number."""

    def test_theMaximumAchievableX(self):
        sol = Solution()
        
        num = 4
        t = 1
        exp = 6
        out = sol.theMaximumAchievableX(num, t)
        self.assertEqual(out, exp)

        num = 3
        t = 2
        exp = 7
        out = sol.theMaximumAchievableX(num, t)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
