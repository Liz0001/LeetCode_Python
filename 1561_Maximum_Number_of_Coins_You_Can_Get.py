import unittest


class Solution:
    def maxCoins(self, piles: [int]) -> int:
        me = 0
        piles = (sorted(piles))
        n = len(piles)
        for i in range(int(n/3), n, 2):
            me+=piles[i]
        return me


class TestSolution(unittest.TestCase):
    """1561. Maximum Number of Coins You Can Get."""

    def test_maxCoins(self):
        sol = Solution()
        
        piles = [2,4,1,2,7,8]
        exp = 9
        out = sol.maxCoins(piles)
        self.assertEqual(exp, out)
        
        piles = [2,4,5]
        exp = 4
        out = sol.maxCoins(piles)
        self.assertEqual(exp, out)
        
        piles = [9,8,7,6,5,1,2,3,4]
        exp = 18
        out = sol.maxCoins(piles)
        self.assertEqual(exp, out)


if __name__ == '__main__':
    unittest.main()
