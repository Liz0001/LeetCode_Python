import unittest

pr = print()

class Solution:
    
    def maxIncreaseKeepingSkyline(self, grid: [[int]]) -> int:
        ng = []
        def get_col(col_nr):
            c = []
            for i in grid:
                c.append(i[col_nr])
            return c

        old = 0
        for i in range(len(grid)):
            old += sum(grid[i])
            n = []
            for j in range(len(grid)):
                row_max = max(grid[i])
                col_max = max(get_col(j))
                n.append(min(row_max, col_max))
            ng.append(n)
            
        new = 0
        for i in range(len(grid)):
            new += sum(ng[i])
        
        return new - old
 

class TestSolution(unittest.TestCase):
    """807. Max Increase to Keep City Skyline."""

    def test_maxIncreaseKeepingSkyline(self):
        sol = Solution()

        grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
        exp = 35
        out = sol.maxIncreaseKeepingSkyline(grid)
        self.assertEqual(out, exp)

        grid = [[0,0,0],[0,0,0],[0,0,0]]
        exp = 0
        out = sol.maxIncreaseKeepingSkyline(grid)
        self.assertEqual(out, exp)
        

if __name__ == "__main__":
    unittest.main()
