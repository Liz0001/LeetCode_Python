from typing import List
import unittest


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.arr = rectangle


    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        arr = self.arr
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                arr[i][j] = newValue


    def getValue(self, row: int, col: int) -> int:
        return self.arr[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)


class TestSubrectangleQueries(unittest.TestCase):
    """1476. Subrectangle Queries."""

    def test_updateSubrectangle(self):
        input = [[1,2,1],[4,3,4],[3,2,1],[1,1,1]]
        exp = [None,1,None,5,5,None,10,5]
        sq = SubrectangleQueries(input)
        
        out = sq.getValue(0,2)
        self.assertEqual(exp[1], out)
        sq.updateSubrectangle(0,0,3,2,5)        
        out = sq.getValue(0,2)
        self.assertEqual(exp[3], out)
        out = sq.getValue(3,1)
        self.assertEqual(exp[4], out)
        sq.updateSubrectangle(3,0,3,2,10)
        out = sq.getValue(3,1)
        self.assertEqual(exp[6], out)
        out = sq.getValue(0,2)
        self.assertEqual(exp[7], out)
 
 
if __name__ == '__main__':
    unittest.main()
