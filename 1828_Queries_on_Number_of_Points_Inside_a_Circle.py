import unittest


class Solution:
    def countPoints(self, points: [[int]], queries: [[int]]) -> [int]:
        answer = []
        for q in queries:
            x = q[0]
            y = q[1]
            c = 0
            for p in points:
                if ((p[0] - x)**2 + (p[1] - y)**2) <= q[2]**2: 
                    c += 1
            answer.append(c)       
                    
        return answer


class TestSolution(unittest.TestCase):
    """1828. Queries on Number of Points Inside a Circle."""

    def test_countPoints(self):
        sol = Solution()

        points = [[1,3],[3,3],[5,3],[2,2]]
        queries = [[2,3,1],[4,3,1],[1,1,2]]
        exp = [3,2,2]
        out = sol.countPoints(points, queries)
        self.assertEqual(exp, out)

        points = [[1,1],[2,2],[3,3],[4,4],[5,5]]
        queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
        exp = [2,3,2,4]
        out = sol.countPoints(points, queries)
        self.assertEqual(exp, out)
        

if __name__ == '__main__':
    unittest.main()
