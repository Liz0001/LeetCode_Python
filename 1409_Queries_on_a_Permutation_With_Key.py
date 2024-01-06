import unittest


class Solution:
    def processQueries(self, queries: [int], m: int) -> [int]:
        p = [*range(1, m+1)]
        pos = []
        for q in queries:
            pos.append(p.index(q))
            p.insert(0, p.pop(p.index(q)))
        return pos


class TestSolution(unittest.TestCase):
    """1409. Queries on a Permutation With Key."""

    def test_processQueries(self):
        sol = Solution()

        queries = [3,1,2,1]
        m = 5
        exp = [2,1,2,1]
        out = sol.processQueries(queries, m)
        self.assertEqual(exp, out)
        
        queries = [4,1,2,2]
        m = 4
        exp = [3,1,2,0]
        out = sol.processQueries(queries, m)
        self.assertEqual(exp, out)

        queries = [7,5,5,8,3]
        m = 8
        exp = [6,5,0,7,5]
        out = sol.processQueries(queries, m)
        self.assertEqual(exp, out)


if __name__ == '__main__':
    unittest.main()
