"""
2373. Largest Local Values in a Matrix from Leetcode.

You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.
"""
from typing import List


class Solution:
    """Largest Local Values in a Matrix Class."""

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        """Largest Local Values in a Matrix."""
        new = []
        for i in range(0, len(grid)-2):
            new2 = []
            for j in range(0, len(grid)-2):
                k = []
                k.append(grid[i][j]),
                k.append(grid[i][j+1]),
                k.append(grid[i][j+2]),
                k.append(grid[i+1][j]),
                k.append(grid[i+1][j+1]),
                k.append(grid[i+1][j+2]),
                k.append(grid[i+2][j]),
                k.append(grid[i+2][j+1]),
                k.append(grid[i+2][j+2])
                new2.append(max(k))
            new.append(new2)
        return new


def main():
    """Solution."""
    s = Solution()
    grid = [
        [9, 9, 8, 1],
        [5, 6, 2, 6],
        [8, 2, 6, 4],
        [6, 2, 2, 2]
        ]
    answer = s.largestLocal(grid)
    print(answer)   # [[9,9],[8,6]]


if __name__ == "__main__":
    main()
