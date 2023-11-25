import unittest
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        





class TestSolution(unittest.TestCase):
    """841. Keys and Rooms"""
    
    def test_canVisitAllRooms(self):
        sol = Solution()
        
        rooms = [[1],[2],[3],[]]
        exp = True
        out = sol.canVisitAllRooms(rooms)
        # self.assertEqual(out, exp)
        
        # rooms = [[1,3],[3,0,1],[2],[0]]
        # exp = True
        # out = sol.canVisitAllRooms(rooms)
        # self.assertEqual(out, exp)


if __name__ == "__main__":
    unittest.main()
