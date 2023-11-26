from typing import List
import unittest


class Solution:
    def canVisitAllRooms(self, r: List[List[int]]) -> bool:
        rooms = {}
        visited = [0]
        for i in range(len(r)):
            rooms[i] = r[i]
        
        for i in visited:
            for j in rooms.get(i):
                if j not in visited:
                    visited.append(j)
        return len(set(visited)) == len(r)


class TestSolution(unittest.TestCase):
    """841. Keys and Rooms"""
    
    def test_canVisitAllRooms(self):
        sol = Solution()
        
        rooms = [[1],[2],[3],[]]
        exp = True
        out = sol.canVisitAllRooms(rooms)
        self.assertEqual(out, exp)
        
        rooms = [[1,3],[3,0,1],[2],[0]]
        exp = False
        out = sol.canVisitAllRooms(rooms)
        self.assertEqual(out, exp)
        
        rooms = [[2],[],[1]]
        exp = True
        out = sol.canVisitAllRooms(rooms)
        self.assertEqual(out, exp)


if __name__ == "__main__":
    unittest.main()
