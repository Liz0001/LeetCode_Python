import unittest


class Solution:
    def onesMinusZeros(self, grid: [[int]]) -> [[int]]:
        diff = []
        ones_row = {}
        ones_col = {}
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            ones_row[i] = grid[i].count(1)
        for i in range(m):
            ones_col[i] = [row[i] for row in grid].count(1)
        
        for i in ones_row:
            d = []
            for j in ones_col:
                d.append(ones_row[i] + ones_col[j] - (n-ones_row[i]) - (m-ones_col[j]))
            diff.append(d)
            
        return diff


class TestSolution(unittest.TestCase):
    """2482. Difference Between Ones and Zeros in Row and Column."""

    def test_onesMinusZeros(self):
        sol = Solution()

        grid = [[0,1,1],[1,0,1],[0,0,1]]
        exp = [[0,0,4],[0,0,4],[-2,-2,2]]
        out = sol.onesMinusZeros(grid)
        self.assertEqual(exp, out)

        grid = [[1,1,1],[1,1,1]]
        exp = [[5,5,5],[5,5,5]]
        out = sol.onesMinusZeros(grid)
        self.assertEqual(exp, out)


if __name__ == '__main__':
    unittest.main()
