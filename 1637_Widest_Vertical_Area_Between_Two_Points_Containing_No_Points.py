import unittest


class Solution:
    def maxWidthOfVerticalArea(self, points: [[int]]) -> int:
        px = [i[0] for i in points]
        pxs = sorted(set(px))
        ans = 0
        for i in range(1, len(pxs)):
            ans = max(ans, abs(pxs[i]-pxs[i-1]))
        return ans


class TestSolution(unittest.TestCase):
    """1637. Widest Vertical Area Between Two Points Containing No Points."""

    def test_maxWidthOfVerticalArea(self):
        sol = Solution()

        points = [[8,7],[9,9],[7,4],[9,7]]
        exp = 1
        out = sol.maxWidthOfVerticalArea(points)
        self.assertEqual(out, exp)

        points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
        exp = 3
        out = sol.maxWidthOfVerticalArea(points)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
