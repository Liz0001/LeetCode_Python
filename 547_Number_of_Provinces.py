from typing import List
import unittest


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province_count = 0
        visited = set()
        
        def dfs(city):
            visited.add(city)
            
            for c in range(len(isConnected)):
                if isConnected[city][c] and c not in visited:
                    dfs(c)
            
            
        for start in range(len(isConnected)):
            if start not in visited:
                province_count += 1
                dfs(start)
        
        print("Province count:", province_count)
        return province_count
        

class TestSolution(unittest.TestCase):
    """547. Number of Provinces"""
    
    def test_findCircleNum(self):
        sol = Solution()

        isConnected = [[1,1,0],
                       [1,1,0],
                       [0,0,1]]
        exp = 2
        out = sol.findCircleNum(isConnected)
        self.assertEqual(out, exp)
        
        isConnected = [[1,0,0],
                       [0,1,0],
                       [0,0,1]]
        exp = 3
        out = sol.findCircleNum(isConnected)
        self.assertEqual(out, exp)

        isConnected = [[1,0,0,1],
                       [0,1,1,0],
                       [0,1,1,1],
                       [1,0,1,1]]
        exp = 1
        out = sol.findCircleNum(isConnected)
        self.assertEqual(out, exp)
        
        isConnected = [[1,1,1,1,1],
                       [1,1,1,1,1],
                       [1,1,1,1,1],
                       [1,1,1,1,1],
                       [1,1,1,1,1]]
        exp = 1
        out = sol.findCircleNum(isConnected)
        self.assertEqual(out, exp)
        
        isConnected = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]
        exp = 3
        out = sol.findCircleNum(isConnected)
        self.assertEqual(out, exp)


if __name__ == "__main__":
    unittest.main()
