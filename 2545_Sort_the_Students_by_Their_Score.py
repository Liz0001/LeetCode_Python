from typing import List
import unittest


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        d = {}
        ans = []
        for s in score:
            d[s[k]] = s
        keys = sorted(list(d.keys()), reverse=True)
        for i in keys:
            ans.append(d[i])
        return ans


class TestSolution(unittest.TestCase):
    """2545. Sort the Students by Their Kth Score."""

    def test_sortTheStudents(self):
        sol = Solution()
        
        score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
        k = 2
        exp = [[7,5,11,2],[10,6,9,1],[4,8,3,15]]
        out = sol.sortTheStudents(score, k)
        self.assertEqual(exp, out)
        
        score = [[3,4],[5,6]]
        k = 0
        exp = [[5,6],[3,4]]
        out = sol.sortTheStudents(score, k)
        self.assertEqual(exp, out)


if __name__ == '__main__':
    unittest.main()
