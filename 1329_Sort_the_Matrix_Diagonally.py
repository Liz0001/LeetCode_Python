from typing import List
import unittest


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = {}
        for z in range(0,(len(mat)+len(mat[0]))-1):
            d[z] = []
            
        r = 0
        for k in range(len(mat)-1, -1, -1):
            for l in range(0, len(mat[0])):
                d[r].append(mat[k][l])
                d[r].sort()
                r+=1
            r -= len(mat[0])-1
            
        q = 0
        for k in range(len(mat)-1, -1, -1):
            for l in range(0, len(mat[0])):
                mat[k][l] = d[q].pop(-1)
                q+=1
            q -= len(mat[0])-1

        return mat


class TestSolution(unittest.TestCase):
    """1329. Sort the Matrix Diagonally."""

    def test_diagonalSort(self):
        sol = Solution()

        mat = [[3,3,1,1],
               [2,2,1,2],
               [1,1,1,2]]
        
        exp = [[1,1,1,1],
               [1,2,2,2],
               [1,2,3,3]]
        out = sol.diagonalSort(mat)
        self.assertEqual(out, exp)

        mat = [[11,25,66,1,69,7],
               [23,55,17,45,15,52],
               [75,31,36,44,58,8],
               [22,27,33,25,68,4],
               [84,28,14,11,5,50]]
        exp = [[5, 17, 4, 1,52, 7],
               [11,11,25,45, 8,69],
               [14,23,25,44,58,15],
               [22,27,31,36,50,66],
               [84,28,75,33,55,68]]
        out = sol.diagonalSort(mat)
        self.assertEqual(out, exp)
        
        mat = [[75,21,13,24,8],
               [24,100,40,49,62]]
        exp = [[75,21,13,24,8],
               [24,100,40,49,62]]
        out = sol.diagonalSort(mat)
        self.assertEqual(out, exp)


if __name__ == '__main__':
    unittest.main()
