import unittest
from typing import List


class Solution:
    def equalPairs(self, g: List[List[int]]) -> int:
        n = len(g)
        count = 0
        cols = [[row[i] for row in g] for i in range(n)]
        for i in g:
            count+= cols.count(i)
        return count


class TestSolution(unittest.TestCase):
    """2352. Equal Row and Column Pairs."""
    def test_equalPairs(self):
        sol = Solution()
        grid = [[3,2,1], [1,7,6], [2,7,7]]
        ans = sol.equalPairs(grid)
        # print("1:", ans)
        self.assertEqual(ans, 1)

        grid = [[3,1,2,2], [1,4,4,5], [2,4,2,2], [2,4,2,2]]
        ans = sol.equalPairs(grid)
        # print("2:", ans)
        self.assertEqual(ans, 3)

        grid =  [[2,1],[1,34]]
        ans = sol.equalPairs(grid)
        # print("3:", ans)
        self.assertEqual(ans, 2)
        
        grid = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]
        ans = sol.equalPairs(grid)
        # print("4:", ans)
        self.assertEqual(ans, 3)


if __name__ == '__main__':
    unittest.main()
